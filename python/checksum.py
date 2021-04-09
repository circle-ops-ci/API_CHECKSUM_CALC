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

def build_checksum(params, secret, ts, r):
    params.append('t=%d' % ts)
    params.append('r=%s' % r)
    params.sort()
    params.append('secret=%s' % secret)
    h = sha256()
    h.update(('&'.join(params)).encode('utf-8'))
    return h.hexdigest()

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

def main():
    example1()
    example2()

if __name__ == "__main__":
    main()