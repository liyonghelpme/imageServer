# -*- coding: utf8 -*-
from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename
import os

DEBUG=True
app = Flask(__name__)
app.config.from_object(__name__)

def transFile(cur):
    allF = os.listdir(cur)
    mvFiles = []
    for i in allF:
        fn = os.path.join(cur, i)
        if os.path.isdir(fn):
            transFile(fn)
        elif i.find('.png') != -1 or i.find('.jpg') != -1 or i.find('.mp3') != -1 or i.find('.fnt') != -1 or i.find(".plist") != -1:
            os.system('python genMd5.py %s; mv %s ../images' % (fn, fn))
            mvFiles.append(i)
    print "mvFiles", mvFiles
        
@app.route('/', methods=['GET', 'POST'])
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        f = request.files['file']
        fname = secure_filename(f.filename)
        f.save(fname)
        if fname[-4:] == '.zip':
            if os.path.exists('temp'):
                os.system('rm temp -rf')
            os.system('mkdir temp')
            os.system('unzip %s -d temp' % (fname))
            allF = os.listdir('temp')
            cur = 'temp'
            transFile(cur)
            #for i in allF:
            #    if i.find('png') != -1 or i.find('jpg') != -1 or i.find('mp3') != -1:
            #        os.system('python genMd5.py temp/%s; mv temp/%s ../images' % (i, i))
            #    elif os.path.isdir('temp/')
            #os.system('mv temp/* ')
        else:
            os.system('python genMd5.py '+fname+'; mv %s ../images/'%(fname))
        return '成功了'

if __name__ == '__main__':
    app.run(debug=True, port=9999, host='0.0.0.0')

