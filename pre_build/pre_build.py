# -*- coding: utf-8 -*-
# 2018年5月1日 下午3:27
# author: wu_chenxu@126.com

import os
import datetime
import re


target = ['SCL', 'TRPC', 'VLC']
blacklist = {'j0':'j_0', 'j1': 'j_1'}
remove_file_list = ['^_.*', '.*\.mk$', '.*\.bat$']
comment_pattern = '^.*#include.*\"\_.*.h\"'

def replace_var_in_blacklist(file, blacklist):
    '''replace the variable name in blacklist'''

    #print_log("->Handling "+str(file))

    with open(file, 'r+') as f:
        code = f.read()
        f.seek(0, 0)
        tansformedCode = code
        for pattern, replace in blacklist.items():
            #print(f"b:{pattern},  w:{replace}")
            tansformedCode = re.sub(pattern, replace, tansformedCode) 
        #print("====>", replacedStr)
        if tansformedCode != code:
            print_log("|-->transformed.")
        else:
            print_log("|-->No update.")
        f.write(tansformedCode)


def comment_statement(file):
    with open(file, 'r+') as f:
        code = f.readlines()
        f.seek(0, 0)
        for line in code:
            if re.search(comment_pattern, line):
                print("line ", line, "matched")
                f.write("//")
            f.write(line)
        #f.write(tansformedCode)

def print_log(*args):
    print(datetime.datetime.now(), end=' ')
    print(*args)




def delete_files():
    list_dirs = os.walk('./')
    for root, dirs, files in list_dirs:
        for f in files:
            print_log("-> "+os.path.join(root, f))
            file_deleted = False
            for pattern in remove_file_list:
                if re.search(pattern, f):
                    file_deleted = True
                    os.remove(os.path.join(root, f))
                    print_log("->>> file removed.")
                    break

def edit_files():
    list_dirs = os.walk('./')
    for root, dirs, files in list_dirs:
        for f in files:
            print_log("-> "+os.path.join(root, f))
            file_suffix = os.path.splitext(f)[1]
            #print(f"suffix: {file_suffix}")
            if file_suffix == '.c' or file_suffix == '.h':
                replace_var_in_blacklist(os.path.join(root, f), blacklist) 
                comment_statement(os.path.join(root, f)) 

print("===========step1: delete files===========")
delete_files()
print("===========step2: replace word in balcklist===========")
edit_files()




