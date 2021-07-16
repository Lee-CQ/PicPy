#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File Name  : PicPy
@Author     : LeeCQ
@Date-Time  : 2021/7/11 23:30
"""
from pathlib import Path
from argparse import ArgumentParser

from requests import post


def img_upload(file_path):
    _f = Path(file_path)
    files = {"file": (_f.name, _f.open('rb'), "image/jpeg")}
    return post('http://img.p.leecq.cn:8080/upload', files=files)


def args_from_cli():
    """解析命令行参数"""
    p_args = ArgumentParser(description='Python图片上传接口')
    p_args.add_argument('file_path', help='文件的绝对路径')
    return p_args.parse_args()


def main():
    """MAN"""
    _args = args_from_cli()
    _http = img_upload(_args.file_path)
    if _http.status_code == 200:
        return _http.text
    else:
        raise Exception(f'{_http.status_code}:  {_http.text}')


if __name__ == '__main__':
    print(main())
