# -*- coding: utf-8 -*-
# 2018年4月30日 下午6:34
# author: wu_chenxu@126.com

#read, write file

import sys

if len(sys.argv) < 2:
    print("Usage python3 ex16.py filename")
    sys.exit(-1)

filename = sys.argv[1]

input(
f'''we're going to erase {filename}.
If you don't want that, hit CTRL-C(^C). If you want that, hit RETURN.
?''')

print("Opening the file...")

f_file = open(filename, 'w')

print("Truncating the file. Goodbye!")
f_file.truncate()

print("Now I\'m going to ask you for three lines.")
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I\'m going to write these to the file.")

f_file.write(line1+'\n'+line2+'\n'+line3+'\n')

print("And finally, we close it.")

f_file.close()








