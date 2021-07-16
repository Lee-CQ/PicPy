#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File Name  : ftplib
@Author     : LeeCQ
@Date-Time  : 2021/7/11 16:38
"""
from ftplib import FTP

from common import AbsLib

with FTP(host='t.leecq.cn', user='img_test', passwd='ftp_p') as ftp:
    ftp.storbinary('STOR img_name', open('/tmp/py-image/8b6e58dfec10ac46cc1036b0e851696e', 'rb'))


class ImageFTP(AbsLib):

    def __init__(self, host, port, user, passwd, to_path):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.to_path = to_path

        self.ftp = FTP()
        self.ftp.connect(self.host, self.port)
        self.ftp.login(user=self.user, passwd=self.passwd)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ftp.close()

    def set_to_path(self, to_path):
        self.to_path = to_path

    def upload_file(self, file, message=''):
        """
        :param message:
        """
        return self.ftp.storbinary(f'STOR {name}', open(name, 'rb'))

    def download_file(self, name):
        return self.ftp.retrbinary(f'RETR {name}', open(name, 'wb').write)
