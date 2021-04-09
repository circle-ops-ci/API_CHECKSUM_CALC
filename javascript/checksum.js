// Copyright (c) 2018-2021 The CYBAVO developers
// All Rights Reserved.
// NOTICE: All information contained herein is, and remains
// the property of CYBAVO and its suppliers,
// if any. The intellectual and technical concepts contained
// herein are proprietary to CYBAVO
// Dissemination of this information or reproduction of this materia
// is strictly forbidden unless prior written permission is obtained
// from CYBAVO.

const crypto = require('crypto');

function buildChecksum(params, secret, t, r) {
  const p = params || [];
  p.push(`t=${t}`, `r=${r}`);
  p.sort();
  p.push(`secret=${secret}`);
  return crypto.createHash('sha256').update(p.join('&')).digest('hex');
}

function example1()
{
    // calculate the checksum for /v1/sofa/wallets/689664/notifications?from_time=1561651200&to_time=1562255999&type=2

    // params contains all query strings and post body if any
    const params = ['from_time=1561651200', 'to_time=1562255999', 'type=2'];

    const curTime = Math.floor(Date.now()/1000);
    const checksum = buildChecksum(params, "THIS_IS_A_SECRET", curTime, "THIS_IS_A_RANDOM_STRING");

    console.log(checksum);
}

function example2()
{
    // calculate the checksum for /v1/sofa/wallets/689664/autofee
    // post body: {"block_num":1}

    // params contains all query strings and post body if any
    const params = ['{"block_num":1}'];

    const curTime = Math.floor(Date.now()/1000);
    const checksum = buildChecksum(params, "THIS_IS_A_SECRET", curTime, "THIS_IS_A_RANDOM_STRING");

    console.log(checksum);
}

example1();
example2();