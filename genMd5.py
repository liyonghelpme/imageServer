import os
import sys
import hashlib
npic = sys.argv[1]

f = open('ser.ini')
images = {}
for l in f.readlines():
    res = l.split('=')
    images[res[0]] = res[1].replace('\n', '')
f.close()

p = open(npic)
con = p.read()
p.close()

v = hashlib.md5(con)
images[npic] = v.hexdigest()

import time
s = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
os.system('mv ser.ini ser.ini-'+s)
nf = open('ser.ini', 'w')
first = True
for k in images:
    if first:
        nf.write('%s=%s'%(k, images[k]))
        first = False
    else:
        nf.write('\n%s=%s'%(k, images[k]))
nf.close()
