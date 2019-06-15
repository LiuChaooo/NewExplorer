# -*- coding: utf-8 -*-
"""
Cryptography, address, transaction manipulation for newchain.
"""
__copyright__ = """ Copyright (c) 2018 Newton Foundation. All rights reserved."""
__version__ = '1.0'
__author__ = 'yanhang@diynova.com'


import base58
from django.conf import settings

class NewChainAddress(object):
    def __init__(self):
        self.chainID = settings.CHAIN_ID
        self.PREFIX = 'NEW'

    def address_encode(self, address_data):
        if address_data.startswith('0x'):
            address_data = address_data[2:]
        hex_chainID = hex(self.chainID)[2:]
        if len(hex_chainID) < 4:
            hex_chainID = '0' + hex_chainID
        num_sum = hex_chainID + address_data
        # data = base58.b58encode_check(b'\0' + num_sum.decode('hex'))
        data = hex(int(num_sum,16))
        new_address = self.PREFIX + data
        return new_address


    def b58check_decode(self, new_address):
        #return Demo: 0xa2f468e8e2f8108e0fdfbf5f8ccad7e571cddd1b
        """ Decoding function """
        # new_address = base58.b58decode_check(bytes(new_address[3:]))
        # address_data = '0x' + new_address.encode('hex')[6:]
        # return address_data
        return '0x' + new_address[8:]

    def is_valid_address(self, new_address):
        new_address = base58.b58decode_check(bytes(new_address[3:]))
        return int(new_address.encode('hex')[:6], 16) == self.chainID

"""
def NewToEth(str):
	print("Str: 0x%s" % base58.b58decode_check(str[3:]).hex().lower()[6:])
	return "0x%s" % base58.b58decode_check(str[3:]).hex().lower()[6:]

def b58check_decode(new_address):
    print(int(new_address[3:],16))
    new_address = '0x' + hex(int(new_address[3:],16))
    return new_address

if __name__ == "__main__":
    new_address = 'NEW132APq4ipFz774M9AsvdY9zkJweSKAsV2n4Mm'
    print(new_address)
    print(NewToEth(new_address))
    # new_address = address_encode(new_address)
    decode_result = b58check_decode('NEW132APq4ipFz774M9AsvdY9zkJweSKAsV2n4Mm')
    print(decode_result)
"""

