#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File Name  : picgo
@Author     : LeeCQ
@Date-Time  : 2021/6/25 22:44
"""
import os

node_url = 'https://npm.taobao.org/mirrors/node/v16.4.0/node-v16.4.0-linux-x64.tar.gz'
node_bin = '/home/py-image/node/bin/node'
npm_bin = '/home/py-image/node/bin/npm'
picgo_bin = '/home/py-image/node/package/lib/node_modules/picgo/bin/picgo'


def install_node():
    os.system('cd ~ ;'
              f'wget {node_url};'
              f'tar -xzvf {node_url.split("/")[-1]} && rm -f {node_url.split("/")[-1]}; '
              f'rm -rf node/; mv node*/ node'
              )
    return True if not os.system(f'{node_bin} -v') else False


def config_npm():
    """配置NPM"""
    os.system(f'{npm_bin} config set registry "https://registry.npm.taobao.org/";'
              f'{npm_bin} config set prefix ~/node/')


def install_package(name):
    os.system(f'{npm_bin} install {name} -g')


def install_picgo_plugin(name):
    os.system(f'')


def env_init():
    if os.system(f'{node_bin} -v'):
        install_node()
        env_init()
    config_npm()
    install_package('picgo')
    return True if not os.system(f'{picgo_bin} -v') else False


if __name__ == '__main__':
    print(env_init())
