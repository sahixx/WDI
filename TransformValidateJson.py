
# -*- coding: utf-8 -*-
import os
import json

filename1 = 'specTablesConsistent'
# filename1 = 'offers_english.json'

urls = []
kvs=[]


def readInChunks(fileObj, chunkSize=1024):
    """
    Lazy function to read a file piece by piece.
    Default chunk size: 4kB.
    """
    while 1:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data


with open('wfp.txt','a',encoding='utf-8') as wfp:
    wfp.write('[')

f = open(filename1,encoding='utf-8')
i=0
for chuck in readInChunks(f):
    i+=1
    #do_something(chunk)
    chuck=chuck.replace('}}\n{','}},\n{')
    print(i,chuck)
    with open('wfp.txt','a',encoding='utf-8') as wfp:
        wfp.write(chuck)

f.close()

with open('wfp.txt','a',encoding='utf-8') as wfp:
    wfp.write(']')

