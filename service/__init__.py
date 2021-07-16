#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File Name  : __init__.py
@Author     : LeeCQ
@Date-Time  : 2021/6/23 23:48
"""
from common import *
from conf import repository


def load_pic(path):
    """入口

    :param path:
    :return:
    """
    if not isinstance(path, Path):
        if isinstance(path, str):
            path = Path(path)
        else:
            raise TypeError(f'仅支持 str 或 Path， 但是收到{path}({type(path)})')

    file_id = md5_file(path)
    pic_byte = path.read_bytes()

    try:

        return file_id
    except:
        pass
