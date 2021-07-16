#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File Name  : lib_other
@Author     : LeeCQ
@Date-Time  : 2021/7/11 19:42


"""
from common import AbsLib


class ImageUFile(AbsLib):
    """UFile 公共库"""

    def __init__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def upload_file(self, file, message=''):
        """
        :param message:
        """


class ImageFTPOD(AbsLib):
    """U-FIle云链 - 最长30天
    1 天  9999次: http://91io.cn/s/xBX1Mi7

GET https://ftpod.cn/uploadSession?fileName=Qingming2021_ZH-CN6154314555_1920x1080.jpg&fileSize=105310&validDays=1&allowDownloadsNum=9999 HTTP/1.1
Host: ftpod.cn
Connection: keep-alive
sec-ch-ua: " Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"
Accept: application/json, text/plain, */*
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://ftpod.cn/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: UM_distinctid=17a9571435c14b-07488eb5ad67e8-7a697e6e-1fa400-17a9571435ddf7; CNZZDATA1278978690=752901988-1625999850-%7C1625999850

HTTP/1.1 200
Server: FunCDN/1.0.1
Date: Sun, 11 Jul 2021 12:16:05 GMT
Content-Type: application/json
Connection: keep-alive
Vary: Accept-Encoding
Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept, token
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS, PATCH
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 3600
Via: edge-55-MISS
Alt-Svc: h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
Content-Length: 1372

{"uploadUrl":"https://xmyp23-my.sharepoint.cn/personal/admin_xmyp23_partner_onmschina_cn/_api/v2.0/drive/items/01QLQIUT5DJTHUD6UNZNDZUDG2TN2Z7SOI/uploadSession?guid='a5ff8960-6acb-4eeb-bba3-9f924239333b'&overwrite=True&rename=False&dc=0&tempauth=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAveG15cDIzLW15LnNoYXJlcG9pbnQuY25ANGQ3MTRmYWYtYTIzNi00OWY5LWExY2YtNWJhMGEyZTQyNzljIiwiaXNzIjoiMDAwMDAwMDMtMDAwMC0wZmYxLWNlMDAtMDAwMDAwMDAwMDAwIiwibmJmIjoiMTYyNjAwNTc2MCIsImV4cCI6IjE2MjYwOTIxNjAiLCJlbmRwb2ludHVybCI6InZoVmkwMHZZbW1pRUV5Z1NPNnVDM3FDNjQ2VlNPVlVBSjY4RmVyN1c0NEU9IiwiZW5kcG9pbnR1cmxMZW5ndGgiOiIyMjIiLCJpc2xvb3BiYWNrIjoiVHJ1ZSIsImNpZCI6Ik9EaGxZbUptTm1RdE9ESTJZaTAwT0RCaExXSm1ZbVV0Wm1WaFlUVmlZbVU1TW1RMyIsInZlciI6Imhhc2hlZHByb29mdG9rZW4iLCJzaXRlaWQiOiJaREEwTkRSalptUXRaalUyT0MwMFptTTFMV0l4TVRndE9EVXhZemxpT1RVeVlXSTUiLCJhcHBfZGlzcGxheW5hbWUiOiJ6ZmlsZSIsImFwcGlkIjoiNGE3MmQ5MjctMTkwNy00ODhkLTllYjItMWI0NjVjNTNjMWM1IiwidGlkIjoiNGQ3MTRmYWYtYTIzNi00OWY5LWExY2YtNWJhMGEyZTQyNzljIiwidXBuIjoiYWRtaW5AeG15cDIzLnBhcnRuZXIub25tc2NoaW5hLmNuIiwicHVpZCI6IjEwMDMzMjMwQzVBN0ZCNjYiLCJjYWNoZWtleSI6IjBoLmZ8bWVtYmVyc2hpcHwxMDAzMzIzMGM1YTdmYjY2QGxpdmUuY29tIiwic2NwIjoiYWxsZmlsZXMud3JpdGUgYWxscHJvZmlsZXMucmVhZCIsInR0IjoiMiIsInVzZVBlcnNpc3RlbnRDb29raWUiOm51bGx9.WElUL1dPQ0didGVVUlFlTkR6UDJCS3ZhbXNjdkJHQUVybXBmNWJwS2RSTT0","callbackId":221020}

======================================================================================================================

POST https://ftpod.cn/uploadCallback/221020 HTTP/1.1
Host: ftpod.cn
Connection: keep-alive
Content-Length: 0
sec-ch-ua: " Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"
Accept: application/json, text/plain, */*
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67
Origin: https://ftpod.cn
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://ftpod.cn/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: UM_distinctid=17a9571435c14b-07488eb5ad67e8-7a697e6e-1fa400-17a9571435ddf7; CNZZDATA1278978690=752901988-1625999850-%7C1625999850


HTTP/1.1 200
Server: FunCDN/1.0.1
Date: Sun, 11 Jul 2021 12:16:06 GMT
Content-Type: application/json
Connection: keep-alive
Vary: Accept-Encoding
Access-Control-Allow-Origin: https://ftpod.cn
Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept, token
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS, PATCH
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 3600
Via: edge-55-MISS
Alt-Svc: h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
Content-Length: 272

{"msg":"操作成功","code":0,"data":{"fileName":"Qingming2021_ZH-CN6154314555_1920x1080.jpg","fileSize":105310,"fileSizeFormat":"102.842 KB","url":"http://91io.cn/s/xBX1Mi7","uploadDate":"2021-07-11 20:17:45","expireDate":"2021-07-12 20:17:45","allowDownloadsNum":9999}}
    """

    def __init__(self):
        pass

    def upload_file(self, file, message=''):
        pass
