#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import hashlib

'''
Product name: AirMal-v1.0(仮)
Discription: Malware Ditection System for Mobile Platform
Author: Kusama Yoshiki (nickname:yotti)
'''

UPLOAD_FOLDER = '/Users/JPZ24557/Desktop/AirMal' # アップロードしたファイルの置き場所

# ALLOWED_EXTENSIONS = set(['apk','ipa']) # ファイル形式の制限

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 * 1024 # ファイルの最大容量とりあえず50MBにしとく

html = ''' 
    <!doctype html>
    <title>AirMal-v1.0</title>
    <h1>AirMal-v1.0</h1>
    <h3> Mobile Malware Detection System Beta vertion 1.0</h3>
    <h4>現在hashベースのスキャン実装中....</h4>
    <h3>Upload APK or IPA file</h3>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
       ''' 

## hash convert function
def hash_file(file):
    '''hash type; md5, sha1, sha256, sha384 , sha512 '''
    h = hashlib.sha256()
    ## ファイルのオープン
    with open(file,'rb') as files:
        chunk = 0
        while chunk != b'':
            chunk = files.read(1024)
            h.upadte(chunk)
    return h.hexdigest()


'''
##ファイルの形式の制限 とりあえず、テスト段階なので実装しない(実際には実装済み)
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
'''

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file: #and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))# file のセーブ
            return redirect(url_for('uploaded_file', filename=filename)) # filenameのurlにredirdect
    return html

@app.route('/<filename>') #filename のサイトを生成
def uploaded_file(filename):
    return hashlib.sha256(filename.encode('utf-8')).hexdigest()#send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
