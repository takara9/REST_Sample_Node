#!/bin/bash
#
#  RESTクライアント
#

#URI=http://localhost:3000
URI=https://nodehashxx.mybluemix.net


echo "GET  ==============="
curl $URI \
    -v \
    -X GET

echo
echo "POST ==============="
curl $URI/hash \
    -v \
    -u "takara:hogehoge" \
    -d "textbody='Hello world'" \
    -X POST

