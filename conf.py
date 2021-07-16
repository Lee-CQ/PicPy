#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File Name  : conf
@Author     : LeeCQ
@Date-Time  : 2021/6/25 20:33
"""

import logging
import sys
from pathlib import Path

from private_conf import PrivateConf

BASE_DIR = Path(__file__).parent
BASE_HOST = 'http://img.p.leecq.cn:8080'

logger = logging.getLogger("logger")  # 创建实例
formatter = logging.Formatter("[%(asctime)s] < %(funcName)s > [%(levelname)s] %(message)s")
# 终端日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)  # 日志文件的格式
logger.setLevel(logging.DEBUG)  # 设置日志文件等级


#
# file_handler = logging.FileHandler()
# logger.addHandler()


class Repository:
    """"""

    class Local:
        type = 'local'
        used = True
        path = Path(r'/tmp/py-image')

    class Coding(PrivateConf.Coding):
        type = 'git'
        path = PrivateConf.Coding.path
        used = True

        git_url = PrivateConf.Coding.git_url
        git_branch = 'master'
        git_username = PrivateConf.Coding.git_username
        git_token = PrivateConf.Coding.git_token
        git_user = git_username
        git_passwd = git_token

    class Gitee:
        type = 'git'
        path = ''
        used = False

        git_url = ''
        git_branch = 'master'
        git_username = ''
        git_token = ''

    class TestFTP(PrivateConf.TestFTP):
        """
        ftp_host = '' Str
        ftp_port =  Int
        ftp_path = ''
        ftp_user = ''
        ftp_passwd = ''
        """
        type = 'ftp'
        path = ''
        used = True

    class UFile:
        type = 'ftp'
        path = ''
        used = False

        ftp_url = ''
        ftp_dir = ''
        ftp_user = ''
        ftp_passwd = ''

    class AliOOS:
        type = 'ali_oos'
        path = ''
        used = False

        ali_oos_url = ''
        ali_oos_ak = ''
        ali_oos_sk = ''


default_URI = Repository.Coding.path
