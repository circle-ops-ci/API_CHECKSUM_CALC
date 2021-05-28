# Copyright (c) 2018-2021 The CYBAVO developers
# All Rights Reserved.
# NOTICE: All information contained herein is, and remains
# the property of CYBAVO and its suppliers,
# if any. The intellectual and technical concepts contained
# herein are proprietary to CYBAVO
# Dissemination of this information or reproduction of this materia
# is strictly forbidden unless prior written permission is obtained
# from CYBAVO.

from time import time
from hashlib import sha256
import base64

def build_checksum(params, secret, ts, r):
    params.append('t=%d' % ts)
    params.append('r=%s' % r)
    params.sort()
    params.append('secret=%s' % secret)
    h = sha256()
    h.update(('&'.join(params)).encode('utf-8'))
    return h.hexdigest()

def calculate_callback_checksum(payload, secret):
    h = sha256()
    h.update((payload + secret).encode('utf-8'))
    return base64.urlsafe_b64encode(h.digest())

def example1():
    # calculate the checksum for /v1/sofa/wallets/689664/notifications?from_time=1561651200&to_time=1562255999&type=2

    # ps contains all query strings and post body if any
    params = []
    params.append('from_time=1561651200')
    params.append('to_time=1562255999')
    params.append('type=2')

    curTime = int(time())
    checksum = build_checksum(params, 'THIS_IS_A_SECRET', curTime, 'THIS_IS_A_RANDOM_STRING')
    print(checksum)

def example2():
    # calculate the checksum for /v1/sofa/wallets/689664/autofee
    # post body: {"block_num":1}

    # ps contains all query strings and post body if any
    params = []
    params.append('{"block_num":1}')

    curTime = int(time())
    checksum = build_checksum(params, 'THIS_IS_A_SECRET', curTime, 'THIS_IS_A_RANDOM_STRING')
    print(checksum)

def callbackChecksumExample():
    # calculate the checksum for callback notification

    payload = '{"type":3,"serial":90000002382,"order_id":"","currency":"TRX","txid":"9784a194f1ed6680108b9ec4f60f93c891d856b0aa01f78daa237d6e746b454a","block_height":15030279,"tindex":0,"vout_index":0,"amount":"5000000","fees":"0","memo":"","broadcast_at":1621416359,"chain_at":1621416375,"from_address":"TFHN66QLPMPqJdzTNTFTt88WpKSVj1C2bW","to_address":"TC3e9gYQfXwfD7kQt37aBncuZrui428Nmx","wallet_id":515837,"state":3,"confirm_blocks":12,"processing_state":2,"addon":{"address_label":"","fee_decimal":6},"decimal":6,"currency_bip44":195,"token_address":""}';

    checksum = calculate_callback_checksum(payload, 'THIS_IS_A_SECRET');
    print(checksum)

def main():
    example1()
    example2()
    callbackChecksumExample()

if __name__ == "__main__":
    main()