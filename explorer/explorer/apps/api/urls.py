from django.conf.urls import url
from . import apis

urlpatterns = [
    # system
    url(r'^system/ping/$', apis.api_ping),
    url(r'^system/ip/$', apis.api_get_ip),
    url(r'^peer', apis.api_get_peer),
    # block chain
    url(r'^version', apis.api_show_version),
    url(r'^blocks', apis.api_show_blocks),
    url(r'^block-index/(?P<height>[0-9]+)', apis.api_show_block_info_by_height),
    url(r'^block/(?P<blockhash>[0-9a-z]+)', apis.api_show_block_info),
    # transaction
    url(r'^txs', apis.api_show_transactions),
    url(r'^tx/send', apis.api_send_transcation),
    url(r'^tx/(?P<txid>[0-9a-z]+)', apis.api_show_transaction),
    # address
    url(r'^addr/(?P<addr>[0-9a-zA-Z]+)', apis.api_show_addr_summary),

    url(r'^addrs/txs', apis.api_show_transactions_by_addresses),
    url(r'^addrs/(?P<addrs>[0-9a-zA-Z,]+)/txs', apis.api_show_transactions_by_addresses),
    # new tx, block
    url(r'^newtx', apis.api_show_newtx),
    # url(r'^newblock',          'api_show_newblock),
    # misc
    url(r'^sync', apis.api_get_sync),
    url(r'^status', apis.api_get_status),
    url(r'^currency', apis.api_get_currency),
    url(r'^utils/estimatefee', apis.api_get_estimatefee),

    # for mobile client
    url(r'^transactions', apis.api_show_client_transactions),
    url(r'^transaction', apis.api_show_client_transaction),

    url(r'^contracts_list', apis.api_show_contracts_list),
    url(r'^contract/(?P<contractAddr>[0-9a-zA-Z]+)', apis.api_show_contract),
    url(r'^brief', apis.api_home_brief),
]
