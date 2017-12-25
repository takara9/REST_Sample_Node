#!/usr/bin/env python
# coding: utf-8
#
#  RESTクライアント
#
import requests
from requests.auth import HTTPBasicAuth
#url = 'https://nodehashxx.mybluemix.net'

def work(url):
    # GET
    uri = url + "/"
    resp = requests.get(uri)
    #print "GET"
    #print "status_code = ", resp.status_code
    #print "resp = ", resp.text
    #print

    # POST
    uri = url + "/hash"
    json = {'textbody': 'hello world'}
    username = 'takara';
    password = 'hogehoge';
    resp = requests.post(uri,json,auth=HTTPBasicAuth(username, password))

    # 結果表示
    rslt = resp.json()
    #print "POST"
    #print "status_code = ", resp.status_code
    #print "sha1   = ", rslt['sha1']
    #print "sha256 = ", rslt['sha256']
    #print "md5    = ", rslt['md5']

    # 高負荷
    uri = url + '/heavy'
    resp = requests.get(uri)
    #print "GET"
    #print "status_code = ", resp.status_code
    #print "resp = ", resp.text
    #print


if __name__ == '__main__':
    
    url = 'http://127.0.0.1'
    while True:
        for p in range(0,4):
            portno = 3000 + p
            print "p=",portno
            uri = url + ":" + str(portno)
            work(uri)
