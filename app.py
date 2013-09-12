# -*- coding: utf8 -*-
from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        f = request.files['file']
        fname = secure_filename(f.filename)
        f.save(fname)
        os.system('python genMd5.py '+fname)
        return '成功了'
if __name__ == '__main__':
    app.run(debug=True, port=9999, host='0.0.0.0')

