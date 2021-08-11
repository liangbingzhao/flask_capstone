# <script src="*xxx.js"></scirpt>

import time
from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
# 为图片命名
import uuid
import os

# LOAD MODEL
app = Flask(__name__)



# static & xxx.html要改

# 必须要运行的,打开html文件
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# 必须要运行的,打开js文件,运行其中fetch
@app.route('/index.js')
def index_js():
    return send_from_directory('static', 'index.js')

@app.route('/add', methods=['POST'])
def get_picandmusic():
    # first phase
    image = request.files.get('initial_image')
    image_name = 'image.jpg'
    image_path = 'static/images/' + image_name
    music = request.files.get('initial_music')
    music_name = 'music.wav'
    music_path = 'static/music/' + music_name
    image.save(image_path)
    music.save(music_path)
    # # run terminal command
    # os.system('bash evaluate.sh 0 1')

    # # 自己定路径
    # f_in = ''
    # f_out = ''
    # # second phase
    # key1 = 'cd ESRGAN; python3 test.py --f_in {} --f_out {}'.format(f_in, f_out)
    # os.system(key1)

    # # third phase
    # key2= ''
    # os.system(key2)

    # # fourth phase
    # os.system()


    music_image_path = 'static/musicimg/2.jpg'
    image_final_path = 'static/finalimg/1.jpg'
    return jsonify({'code': 0, 'msg': 'Success',  'image_final_url':image_final_path, 'music_image_url':music_image_path})

app.run(host='127.0.0.1', port=8000)