#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File Name  : ut
@Author     : LeeCQ
@Date-Time  : 2021/7/11 14:27
"""
import unittest
from pathlib import Path

from service.lib_git import ImageGit

RESOURCE_PATH = Path(__file__).parent.joinpath('resource')
RESOURCE_PATH.mkdir()


class UTGitImage(unittest.TestCase):
    """Git的测试"""


class UTFtpImage(unittest.TestCase):
    """FTP的测试"""


class UTApp(unittest.TestCase):
    """APP的测试"""
