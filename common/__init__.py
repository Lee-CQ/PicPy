#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File Name  : __init__.py
@Author     : LeeCQ
@Date-Time  : 2021/6/23 23:48
"""
import time
import abc
from pathlib import Path
from imghdr import what as _img_what, tests
from hashlib import md5 as _md5


def _img_what_from_stream(_stream):
    """"""


class AbsLib(abc.ABC):

    @abc.abstractmethod
    def upload_file(self, file, message=''):
        """上传文件
        :param file
        :param message:
        :return URL
        """

    def auto_load_config(self, _type):
        pass


def is_img(file: (Path, str)):
    """是否是图片"""

    return True if _img_what(file) else False


def md5_file(file: Path) -> str:
    """返回文件的MD5值"""
    _m = _md5()
    with open(file, 'rb') as fb:
        while True:
            _data = fb.read(20480)
            if not _data:
                break
            _m.update(_data)
    return _m.hexdigest()


def md5_stream(_io):
    _m = _md5()
    _m.update(_io)
    return _m.hexdigest()


def now_timestamp():
    """返回当前时间的时间戳"""
    return int(time.time() * 1000)


if __name__ == '__main__':
    _ = md5_file(Path(r'C:\Users\LCQ\Pictures\Qingming2021_ZH-CN6154314555_1920x1080.jpg'))
    print(_)
