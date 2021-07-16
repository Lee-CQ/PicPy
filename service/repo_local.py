#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File Name  : repo_local
@Author     : LeeCQ
@Date-Time  : 2021/6/25 22:25

本地文件处理: 其实是本地仓库图片处理

本地存储库
"""
from pathlib import Path

from service.lib_git import ImageGit
from common import md5_stream, AbsLib


class ImageLocal(AbsLib):
    """本地图片存储"""

    def __init__(self, to_path, _bytes: bytes, name=None, messages=None):
        self.to_path = to_path
        self.bytes = _bytes
        self.md5 = md5_stream(_bytes)
        self.name = name or self.md5
        self.messages = messages or ''

    def save_photo(self, to_path=None):
        """保存图片到本地存储库"""
        self.to_path = to_path or self.to_path
        Path(self.to_path).joinpath(self.md5).write_bytes(self.bytes)

    def info_to_sql(self):
        """图片信息存储到数据库"""

    def upload_file(self, file=None, message=''):
        """上传文件"""
        self.save_photo()
        ImageGit(to_path=self.to_path).upload_file(file or self.md5, message or self.messages)
