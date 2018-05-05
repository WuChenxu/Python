# -*- coding: utf-8 -*-
# 2018年5月1日 下午3:27
# author: wu_chenxu@126.com

import os
import datetime
import re


TARGET_FOLDER = ['SCL', 'TRPC', 'VLC']
BLACKLIST = {'j0':'j_0', 'j1': 'j_1'}
REMOVE_FILE_LIST = ['^_.*', r'.*\.mk$', r'.*\.bat$']
COMMENT_PATTERN = r'^#include.*\"\_.*.h\"'

def replace_var_in_blacklist(filename, blacklist):
    '''replace the variable name in blacklist'''

    #print_log("->Handling "+str(filename))

    with open(filename, 'r+') as file:
        code = file.read()
        file.seek(0, 0)
        tansformed_code = code
        for pattern, replace in blacklist.items():
            #print(f"b:{pattern},  w:{replace}")
            tansformed_code = re.sub(pattern, replace, tansformed_code)
        #print("====>", replacedStr)
        if tansformed_code != code:
            print_log("|-->transformed.")
        else:
            print_log("|-->No update.")
        file.write(tansformed_code)


def comment_statement(filename):
    with open(filename, 'r+') as file:
        code = file.readlines()
        file.seek(0, 0)
        for line in code:
            if re.search(COMMENT_PATTERN, line):
                print("line ", line, "matched")
                file.write("//")
            file.write(line)


def print_log(*args):
    print(datetime.datetime.now(), end=' ')
    print(*args)




def delete_files():
    list_dirs = os.walk('./')
    for root, _, files in list_dirs:
        for file in files:
            print_log("-> "+os.path.join(root, file))
            for pattern in REMOVE_FILE_LIST:
                if re.search(pattern, file):
                    os.remove(os.path.join(root, file))
                    print_log("->>> file removed.")
                    break

def edit_files():
    list_dirs = os.walk('./')
    for root, _, files in list_dirs:
        for file in files:
            print_log("-> "+os.path.join(root, file))
            file_suffix = os.path.splitext(file)[1]
            #print(f"suffix: {file_suffix}")
            if file_suffix == '.c' or file_suffix == '.h':
                replace_var_in_blacklist(os.path.join(root, file), BLACKLIST)
                comment_statement(os.path.join(root, file))

if __name__ == '__main__':
    print("===========step1: delete files===========")
    delete_files()
    print("===========step2: replace word in balcklist===========")
    edit_files()
