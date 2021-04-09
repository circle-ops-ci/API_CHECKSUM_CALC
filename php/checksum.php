<?php
// Copyright (c) 2018-2021 The CYBAVO developers
// All Rights Reserved.
// NOTICE: All information contained herein is, and remains
// the property of CYBAVO and its suppliers,
// if any. The intellectual and technical concepts contained
// herein are proprietary to CYBAVO
// Dissemination of this information or reproduction of this materia
// is strictly forbidden unless prior written permission is obtained
// from CYBAVO.

function build_checksum($params, $secret, $t, $r) {
    array_push($params, 't='.$t, 'r='.$r);
    sort($params);
    array_push($params, 'secret='.$secret);
    return hash('sha256', implode('&', $params));
}

function example1() {
    // calculate the checksum for /v1/sofa/wallets/689664/notifications?from_time=1561651200&to_time=1562255999&type=2

    // ps contains all query strings and post body if any
    $params = ['from_time=1561651200', 'to_time=1562255999', 'type=2'];

    $curTime = time();
    $checksum = build_checksum($params, "THIS_IS_A_SECRET", $curTime, "THIS_IS_A_RANDOM_STRING");

    file_put_contents('php://stdout', $checksum."\n");
}

function example2() {
    // calculate the checksum for /v1/sofa/wallets/689664/autofee
    // post body: {"block_num":1}

    // ps contains all query strings and post body if any
    $params = ['{"block_num":1}'];

    $curTime = time();
    $checksum = build_checksum($params, "THIS_IS_A_SECRET", $curTime, "THIS_IS_A_RANDOM_STRING");

    file_put_contents('php://stdout', $checksum."\n");
}

example1();
example2();

?>