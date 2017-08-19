#!/usr/bin/env python
# coding: utf-8
#
#  RESTクライアント
#
import requests
from requests.auth import HTTPBasicAuth

#url = 'http://127.0.0.1:3000'
url = 'https://nodehashxx.mybluemix.net'

# GET
uri = url
resp = requests.get(uri)
print "GET"
print "status_code = ", resp.status_code
print "resp = ", resp.text
print


# POST
uri = url + "/hash"
json = {'textbody': 'hello world'}
username = 'takara';
password = 'hogehoge';
resp = requests.post(uri,json,auth=HTTPBasicAuth(username, password))

# 結果表示
rslt = resp.json()
print "POST"
print "status_code = ", resp.status_code
print "sha1   = ", rslt['sha1']
print "sha256 = ", rslt['sha256']
print "md5    = ", rslt['md5']




