#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 13:38:58 2017

@author: jordan
"""

import os
path = ''
def deleteExt(path):
    count = 0
    fileCount = 0
    for root, dirs, files in os.walk(path):
        
        for currentFile in files:
            exts = ['.png', '.jpg', '.bmp', '.ini', '.db', '.lst', '.idx', '.txt', '.d2v']
            fileCount += 1
            print "Processing File:" + currentFile
            
            if any(currentFile.lower().endswith(ext) for ext in exts):
                os.remove(os.path.join(root, currentFile))
                count += 1
                         
    print str(fileCount) + ' files scanned.'            
    print str(count) + ' files deleted.'