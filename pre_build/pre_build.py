# -*- coding: utf-8 -*-
# 2018年5月1日 下午3:27
# author: wu_chenxu@126.com

import os
import datetime
import re


target = ['SCL', 'TRPC', 'VLC']
blacklist = {'j0':'j_0', 'j1': 'j_1'}
remove_file_list = ['^_.*', '.*\.mk$', '.*\.bat$']

def replaceVarInBlacklist(file, blacklist):
    '''
    replace the variable name in blacklist
    '''
    #printLog("->Handling "+str(file))

    with open(file, 'r+') as f:
        code = f.read()
        f.seek(0, 0)
        tansformedCode = code
        for pattern, replace in blacklist.items():
            #print(f"b:{pattern},  w:{replace}")
            tansformedCode = re.sub(pattern, replace, tansformedCode) 
        #print("====>", replacedStr)
        if tansformedCode != code:
            printLog("|-->transformed.")
        else:
            printLog("|-->No update.")
        f.write(tansformedCode)

pat = '^.*#include.*\"\_.*.h\"'
def commentStatement(file):
    with open(file, 'r+') as f:
        code = f.readlines()
        f.seek(0, 0)
        for line in code:
            if re.search(pat, line):
                print("line ", line, "matched")
                f.write("//")
            f.write(line)
        #f.write(tansformedCode)

def printLog(*args):
    print(datetime.datetime.now(), end=' ')
    print(*args)




def deleteFiles():
    list_dirs = os.walk('./')
    for root, dirs, files in list_dirs:
        for f in files:
            printLog("-> "+os.path.join(root, f))
            file_deleted = False
            for pattern in remove_file_list:
                if re.search(pattern, f):
                    file_deleted = True
                    os.remove(os.path.join(root, f))
                    printLog("->>> file removed.")
                    break

def replaceBlacklist():
    list_dirs = os.walk('./')
    for root, dirs, files in list_dirs:
        for f in files:
            printLog("-> "+os.path.join(root, f))
            file_suffix = os.path.splitext(f)[1]
            #print(f"suffix: {file_suffix}")
            if file_suffix == '.c' or file_suffix == '.h':
                replaceVarInBlacklist(os.path.join(root, f), blacklist) 
                commentStatement(os.path.join(root, f)) 

print("===========step1: delete files===========")
deleteFiles()
print("===========step2: replace word in balcklist===========")
replaceBlacklist()




