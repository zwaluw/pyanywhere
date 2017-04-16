
import os
from os import walk
startpath = os.path.dirname(os.path.abspath(__file__))

# f = []
# for (dirpath, dirnames, filenames) in walk(mypath):
#     f.extend(filenames)
    
# print mypath
# dirs = os.listdir(mypath)
# for file in dirs:
# 	print file


import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


list_files(startpath)