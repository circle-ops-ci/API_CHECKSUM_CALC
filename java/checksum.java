// Copyright (c) 2018-2021 The CYBAVO developers
// All Rights Reserved.
// NOTICE: All information contained herein is, and remains
// the property of CYBAVO and its suppliers,
// if any. The intellectual and technical concepts contained
// herein are proprietary to CYBAVO
// Dissemination of this information or reproduction of this materia
// is strictly forbidden unless prior written permission is obtained
// from CYBAVO.

package com.cybavo.api.checksum;

import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class checksum {

    static String sha256(final String input) throws NoSuchAlgorithmException, UnsupportedEncodingException {
        final MessageDigest digest = MessageDigest.getInstance("SHA-256");
        digest.reset();
        digest.update(input.getBytes("utf8"));
        return String.format("%064x", new BigInteger(1, digest.digest()));
    }

    static String buildChecksum(final List<String> params, final String secret, final long time, final String r) throws NoSuchAlgorithmException, UnsupportedEncodingException {
        params.add(String.format("t=%d", time));
        params.add(String.format("r=%s", r));
        Collections.sort(params);
        params.add(String.format("secret=%s", secret));
        return sha256(String.join("&", params));
    }

    static void example1() {
        List<String> params = new ArrayList<String>();
        params.add("from_time=1561651200");
        params.add("to_time=1562255999");
        params.add("type=2");

        try {
            final long curTime = System.currentTimeMillis() / 1000;
            String checksum = buildChecksum(params, "THIS_IS_A_SECRET", curTime, "THIS_IS_A_RANDOM_STRING");
            System.out.println(checksum);
        } catch (final Exception e) {
        }
    }

    static void example2() {
        List<String> params = new ArrayList<String>();
        params.add("{\"block_num\":1}");

        try {
            final long curTime = System.currentTimeMillis() / 1000;
            String checksum = buildChecksum(params, "THIS_IS_A_SECRET", curTime, "THIS_IS_A_RANDOM_STRING");
            System.out.println(checksum);
        } catch (final Exception e) {
        }
    }

    public static void main(String[] args) {
        example1();
        example2();
	}
}
