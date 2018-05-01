# -*- coding: utf-8 -*-
# 2018年4月30日 下午10:46
# author: wu_chenxu@126.com

# copy file

import sys,os

if len(sys.argv) < 3:
    print("Usage: python3 ex17.py from_file.txt to_file.txt")
    exit(-1)

from_file, to_file = sys.argv[1:]

print(f"Copying from {from_file} to {to_file}")

f_from = open(from_file)
indata = f_from.read()

print(f"The input file is {len(indata)} bytes long") 



print(f"Does the output file exist? {os.path.exists(to_file)}")

input("Ready, hit RETURN to continue, CTRL-C to abort")

f_to = open(to_file, 'w+')


f_to.write(indata)

print("Alright, all done.")

f_from.close()
f_to.close()
