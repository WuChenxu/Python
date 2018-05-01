# -*- coding: utf-8 -*-
# 2018年4月30日 下午6:16
# author: wu_chenxu@126.com

#reading file
from sys import argv

if(len(argv)) < 2:
    print("Usage: python3 thi_file.py txt_file")
    exit(1)

filename= argv[1]

f = open(filename)

print(f"Here's your file {filename}:")
print(f.read())

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())


