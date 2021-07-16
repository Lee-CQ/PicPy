#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@File Name  : app
@Author     : LeeCQ
@Date-Time  : 2021/7/10 19:42
"""
from pathlib import Path

from flask import Flask, flash, redirect, url_for, make_response
from flask import request, render_template

from conf import BASE_DIR, Repository, logger, BASE_HOST
from common import is_img, md5_stream
from service.lib_git import ImageGit
from service.repo_local import ImageLocal

app = Flask('Image_Bed')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000  # 最大16M
app.config['UPLOAD_FOLDER'] = Repository.Local.path  # 上传目录
app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'

Path(Repository.Local.path).mkdir(mode=0o700, exist_ok=True)

app.template_folder = BASE_DIR.joinpath('static')
app.static_folder = BASE_DIR.joinpath('template')
app.repo_git = ImageGit(Repository.Local.path).auto_add_remote_from_config()


@app.route('/upload', methods=['POST', 'GET'])
def upload_image():
    """图片上传接口

    :return 一个可以访达的URL；
    """
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # file_b = file.stream.read()
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and is_img(file.stream):
            file_b = file.stream.read()
            file_id = md5_stream(file_b)
            origin_name = file.filename
            ImageLocal(Repository.Local.path, file_b).save_photo()
            app.repo_git.upload_file(file_id, origin_name)
            # TODO 落库
            return BASE_HOST + url_for('img', file_id=file_id)
        else:
            app.logger.error('不是图片')
            return '不是图片'

    return render_template('upload.html')


@app.route('/img/<file_id>', endpoint='img')
def rely_url_302(file_id):
    """对ID进行302重定向！"""
    from conf import default_URI
    return redirect(f'{default_URI}/{file_id}')


@app.route('/local/<file_id>', endpoint='local')
def local_pic(file_id):
    """呈现本地库图片"""
    _res = make_response(Path(app.config['UPLOAD_FOLDER']).joinpath(file_id).read_bytes())
    _res.headers.update({'Content-Type': 'image/png'})

    return _res


if __name__ == '__main__':
    from conf import console_handler

    logger.addHandler(console_handler)
    app.logger.addHandler(console_handler)
    app.template_folder = Path(__file__).parent.joinpath('templates').as_posix()
    app.run(host='0.0.0.0', port=8080, debug=True)
