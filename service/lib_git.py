#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File Name  : gitlib
@Author     : LeeCQ
@Date-Time  : 2021/6/25 22:09
"""
from typing import Union, List
from re import fullmatch

from git import Repo
from git.exc import InvalidGitRepositoryError, GitCommandError

from common import AbsLib
from conf import logger, console_handler, Repository as ConfRepo


class ImageGitRemote:

    def __init__(self, repo: Repo, name, url, branch, user, passwd):
        self.repo = repo
        self.name = name
        self.url = url
        self.branch = branch
        self.user = user
        self.passwd = passwd

        self.add_remote()

    def add_remote(self):
        try:
            self.repo.remote(self.name).remove(self.repo, self.name)
            logger.warning(f'老旧远程仓库已经移除 {self.name}')
        finally:
            self.repo.create_remote(self.name, self.url_with_login)
            logger.info(f'远程存储库添加完成：{self.name}')

    @property
    def url_with_login(self):
        """"""
        __s = not fullmatch(r'http[s]://.*?:.*?@.*?', self.url)
        if __s and self.user and self.passwd:
            _http, _uri = self.url.split('://')
            logger.info('构造了包含用户名和密码的Git URL')
            return f'{_http}://{self.user}:{self.passwd}@{_uri}'
        elif __s and self.user:
            _http, _uri = self.url.split('://')
            logger.info('构造了仅包含用户名的Git URL')
            return f'{_http}://{self.user}@{_uri}'
        else:
            logger.warning(f'没有提供用户名、密码，或用户名密码已经包含在URL中了.')
            return self.url

    def set_users(self, user=None, passwd=None):
        """设置环境变量"""
        self.repo.git.update_environment(GIT_USERNAME=user or self.user,
                                         GIT_PASSWORD=passwd or self.passwd
                                         )

    def pull(self, refspec):
        self.set_users()
        self.repo.remote(self.name).pull(refspec or f'{self.branch}:{self.branch}', )
        logger.info(f'成功 pull Git库：{self.name}:{self.branch} -> {self.branch}')

    def push(self, refspec: Union[str, List[str], None] = None):
        self.set_users()
        self.repo.remote(self.name).push(refspec or f'{self.branch}:{self.branch}', )
        logger.info(f'成功 push Git库：{self.branch} -> {self.name}:{self.branch}')


class ImageGit(AbsLib):
    """Git图片存储"""

    def __init__(self, to_path):
        self.to_path = to_path
        self.remote_repos = []

        try:
            self.repo = Repo(to_path)
        except InvalidGitRepositoryError:  # 无效的Git库目录
            self.repo = Repo.init(to_path)

    def add_remote(self, name, url, branch, user=None, passwd=None):
        """添加一个远程库"""

        self.remote_repos.append(ImageGitRemote(self.repo, name, url, branch, user, passwd))

    def auto_add_remote_from_config(self):
        """自动从配置文件中加入git存储库"""
        for name, _git_repo in ConfRepo.__dict__.items():
            # logger.debug(f'{name}  --- {_git_repo}')
            try:
                if _git_repo.type == 'git' and _git_repo.used:
                    self.add_remote(name, _git_repo.git_url, _git_repo.git_branch,
                                    _git_repo.git_user, _git_repo.git_passwd)
                    logger.info(f'成功添加远程Git存储库：{name} ... ')
                elif _git_repo.type == 'git' and not _git_repo.used:
                    logger.warning(f'{name} 未启用 ！')
                else:
                    logger.error(f'{name} 不是一个有效的Git库！')

            except GitCommandError as _e:
                logger.error(f'添加Git存储库 {name} 失败: {_e}')

            except Exception as _e:
                if name.startswith('__'):
                    continue
                logger.warning(f'{name} 不是一个可用的git存储库 ... {_e}')
        return self

    def pull_from_all_remote(self):
        """从全部远程库拉取"""
        for _repo_remote in self.remote_repos:
            _repo_remote.pull()

    def push_to_all_remote(self):
        """"""
        for _repo_remote in self.remote_repos:
            _repo_remote.push()

    def add_commit(self, file, message):
        """添加并提交一个文件"""
        if file in self.untracked_files:
            self.repo.git.add(file)
            self.repo.index.commit(message)
            logger.info(f'成功添加文件{file}到Git库 ... ')
        else:
            logger.warning(f'文件{file}已经存在于Git库中 ... ')

    @property
    def untracked_files(self):
        """返回未跟踪文件列表"""
        return self.repo.untracked_files

    def upload_file(self, file, message=''):
        self.add_commit(file, message)
        self.push_to_all_remote()


if __name__ == '__main__':
    logger.addHandler(console_handler)

    a = ImageGit('/tmp/py-image')
    a.auto_add_remote_from_config()
    a.add_commit('db3ac18043043298c7c93ed89bd92ce0', '测试2')
    a.push_to_all_remote()
