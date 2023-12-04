# coding:utf-8

from flask import Flask,render_template,request,redirect,url_for,send_from_directory
from werkzeug.utils import secure_filename
import os

download_path=r'D:\fq\2023-2024-1\05A21061\Projects'

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def start():
    if request.method == 'POST':
        print("start→upload")
        return redirect(url_for('upload'))
    return render_template('start.html')

@app.route('/download', methods=['POST', 'GET'])
def download():
    if request.method == 'GET':
        print("start→download")
        return redirect(host='172.30.5.24',port=8869) 
    return send_from_directory(download_path,"/") 

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, r'D:\fq\2023-2024-1\05A21061\Projects',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return redirect(url_for('success'))
    return render_template('upload.html')


@app.route('/success', methods=['POST', 'GET'])
def success():

    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True,host='172.30.5.24',port=5000)