// Copyright (c) 2018-2021 The CYBAVO developers
// All Rights Reserved.
// NOTICE: All information contained herein is, and remains
// the property of CYBAVO and its suppliers,
// if any. The intellectual and technical concepts contained
// herein are proprietary to CYBAVO
// Dissemination of this information or reproduction of this materia
// is strictly forbidden unless prior written permission is obtained
// from CYBAVO.

package main

import (
	"crypto/sha256"
	"fmt"
	"sort"
	"strings"
	"time"
)

func buildChecksum(params []string, secret string, time int64, r string) string {
	params = append(params, fmt.Sprintf("t=%d", time))
	params = append(params, fmt.Sprintf("r=%s", r))
	sort.Strings(params)
	params = append(params, fmt.Sprintf("secret=%s", secret))
	return fmt.Sprintf("%x", sha256.Sum256([]byte(strings.Join(params, "&"))))
}

func example1() {
	// calculate the checksum for /v1/sofa/wallets/689664/notifications?from_time=1561651200&to_time=1562255999&type=2

	// params contains all query strings and post body if any
	params := []string{"from_time=1561651200", "to_time=1562255999", "type=2"}

	curTime := time.Now().Unix()
	checksum := buildChecksum(params, "THIS_IS_A_SECRET", curTime, "THIS_IS_A_RANDOM_STRING")

	fmt.Println(checksum)
}

func example2() {
	// calculate the checksum for /v1/sofa/wallets/689664/autofee
	// post body: {"block_num":1}

	// params contains all query strings and post body if any
	params := []string{`{"block_num":1}`}

	curTime := time.Now().Unix()
	checksum := buildChecksum(params, "THIS_IS_A_SECRET", curTime, "THIS_IS_A_RANDOM_STRING")

	fmt.Println(checksum)
}

func main() {
	example1()
	example2()
}
