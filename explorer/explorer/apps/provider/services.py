"""The implementation of service layer for serveral blockchain information

"""

__copyright__ = """ Copyright (c) 2016 Beijing ShenJiangHuDong Technology Co., Ltd. All rights reserved."""
__version__ = '1.0'
__author__ = 'xiawu@lubangame.com'
import time
import logging
from mongoengine import connect
from django.conf import settings
from django.core.cache import cache
from config import codes
import provider_newton
from provider import models as provider_models
from decimal import *

DECIMAL_SATOSHI = Decimal("100000000")
logger = logging.getLogger(__name__)
blockchain_providers = {
    codes.BlockChainType.NEWTON.value: provider_newton
}

def get_current_height(blockchain_type=codes.BlockChainType.NEWTON.value):
    try:
        obj = provider_models.Block._get_collection().aggregate([
            { "$group": {
                "_id": None,
                "height": { "$max": "$height" }
            }}
        ])
        result = obj['result']
        if not result:
            return -1
        return result[0]['height']
    except Exception, inst:
        print inst
        return -1

def get_current_blockhash(blockchain_type=codes.BlockChainType.NEWTON.value):
    try:
        height = get_current_height(blockchain_type)
        if height < 0:
            return ''
        obj = provider_models.Block.objects.get(height=height)
        return obj.blockhash
    except Exception, inst:
        print inst
        return ""

def get_block_hash_by_height(height, blockchain_type=codes.BlockChainType.NEWTON.value):
    try:
        obj = provider_models.Block.objects.get(height=height)
        return obj.blockhash
    except Exception, inst:
        print inst
        return ''

def store_block_data(block_info, provider, blockchain_type=codes.BlockChainType.NEWTON.value, is_fast_sync=False):
    """Store the block info
    """
    try:
        current_blockhash = get_current_blockhash(blockchain_type)
        previous_blockhash = block_info['previousblockhash']
        if len(current_blockhash) > 0 and current_blockhash != previous_blockhash: # find a block fork
            logger.error("find a block fork at: height %s, current_blockhash %s, previous_blockhash %s" % (block_info['height'], current_blockhash, previous_blockhash))
            return False
        if len(current_blockhash) == 0 and not is_fast_sync: # the db is empty
            logger.info("db is empty...")
            return False
        block_instance = provider_models.Block()
        for k, v in block_info.items():
            setattr(block_instance, k, v)
        txlength = block_instance.txlength
        if txlength > 0:
            # get transactions
            for item in block_info['transactions']:
                tx_item = provider.parse_transaction_response(item)
                transaction_info = tx_item
                txid = transaction_info['txid']
                transaction_instance = provider_models.Transaction()
                for k, v in transaction_info.items():
                    setattr(transaction_instance, k, v)
                transaction_instance.blockhash = block_info['blockhash']
                transaction_instance.blockheight = block_info['height']
                transaction_instance.time = block_info['time']
                transaction_instance.save()
                # indexing address
                obj = provider_models.Address()
                obj.addr = transaction_instance.from_address
                obj.txid = txid
                obj.blockheight = block_info['height']
                obj.value = transaction_instance.value
                obj.vtype = codes.ValueType.SEND.value
                obj.n = transaction_instance.transaction_index
                obj.time = transaction_instance.time
                obj.save()
                obj = provider_models.Address()
                obj.addr = transaction_instance.to_address
                obj.txid = txid
                obj.blockheight = block_info['height']
                obj.value = transaction_instance.value
                obj.vtype = codes.ValueType.RECEIVE.value
                obj.n = transaction_instance.transaction_index
                obj.time = transaction_instance.time
                obj.save()
        # when transaction is finish, store block
        block_instance.save()
        return True
    except Exception, inst:
        print inst
        logger.exception("fail to store block data:%s" % str(inst))
        return False

def delete_data_by_block_height(height):
    provider_models.Block.objects.filter(height__gt=height).delete()
    provider_models.Transaction.objects.filter(blockheight__gt=height).delete()
    provider_models.Address.objects.filter(blockheight__gt=height).delete()

def handle_block_fork(blockchain_type):
    """Handle the block fork
        if it occurs, delete all block data
    """
    try:
        logger.info("start to handle block fork...")
        url_prefix = settings.FULL_NODES['new']['rest_url']
        target_height = 0
        delete_data_by_block_height(target_height)
        sync_blockchain(url_prefix, blockchain_type=blockchain_type, from_height=target_height)
        logger.info("handle block fork successfully.")
        return True
    except Exception, inst:
        print "fail to handle block fork:", str(inst)
        logger.exception("fail to handle block fork: %s" % str(inst))
        return False
    
def sync_block_rawdata(data, blockchain_type=codes.BlockChainType.NEWTON.value):
    """Sync the block raw info
    """
    try:
        provider = blockchain_providers[blockchain_type].Provider('')
        block_info = provider.parse_block_info(data)
        status = store_block_data(block_info)
        if not status:
            handle_block_fork(blockchain_type)
    except Exception, inst:
        print inst
        logger.exception("fail to sync block raw data:%s" % str(inst))

def sync_blockchain(url_prefix, blockchain_type=codes.BlockChainType.NEWTON.value, from_height=None):
    """Sync the blockchain info from full node to database
    """
    try:
        provider = blockchain_providers[blockchain_type].Provider(url_prefix)
        if not from_height:
            # query the current height
            current_height = get_current_height(blockchain_type)
        else:
            current_height = from_height
        logger.info("sync_blockchain:current_height:%s" % current_height)
        # query the height of blockchain
        height = provider.get_block_height()
        if height <= current_height:
            logger.info("sync_blockchain:no new block")
            return
        status = True
        for tmp_height in range(current_height+1, height+1):
            # get block info
            data = provider.get_block_by_height(tmp_height)
            status = store_block_data(data, provider, is_fast_sync=True)
            if not status:
                break
            logger.info("sync_blockchain:height:%s" % tmp_height)
        if not status:
            handle_block_fork(blockchain_type)
    except Exception, inst:
        print "fail to sync blockchain", inst
        logger.exception("fail to sync blockchain:%s" % str(inst))
    
def send_transaction(rawtx, blockchain_type=codes.BlockChainType.NEWTON.value):
    """Send transaction
    
    """
    try:
        url_prefix = settings.FULL_NODES['new']['rest_url']
        provider = blockchain_providers[blockchain_type].Provider(url_prefix)
        return provider.send_transaction(rawtx)
    except Exception, inst:
        print inst
        logger.exception("fail to send transaction:%s" % str(inst))
        return None

def get_transaction_pool(blockchain_type=codes.BlockChainType.NEWTON.value):
    """Get the transaction list in memory pool
    
    """
    try:
        url_prefix = settings.FULL_NODES['new']['rest_url']
        provider = blockchain_providers[blockchain_type].Provider(url_prefix)
        return provider.get_transaction_pool()
    except Exception, inst:
        print inst
        logger.exception("fail to get transaction list in memory pool:%s" % str(inst))
        return []

def parse_transaction_message(data, blockchain_type=codes.BlockChainType.NEWTON.value):
    """Parse the transaction message
    
    """
    try:
        provider = blockchain_providers[blockchain_type].Provider('')
        return provider.parse_transaction_response(data)
    except Exception, inst:
        print inst
        logger.exception("fail to parse transaction message:%s" % str(inst))
        return None

