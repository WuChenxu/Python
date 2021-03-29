
# how to generate static library
```bash
gcc -c c_func.c
ar rcs libmylib.a hello.o
```

# how to generate dynamic library

## from file
```bash
gcc c_func.c -shared -o c_func_dy.so
```
## from static library
```bash
# 先将静态库解出obj文件
$ar -x mylib.a
 # 再用gcc 将obj文件，编译成动态库
$gcc -shared -fPIC *.o -o mylib.so
```

# how to call C API
call_c_func.py


reference:
1. [Python Bindings: Calling C or C++ From Python](https://realpython.com/python-bindings-overview/#python-bindings-overview)
2. [-fpic 与-fPIC的区别](https://blog.csdn.net/xiangguiwang/article/details/81939237)
3. [Linux下Gcc生成和使用静态库和动态库详解](http://blog.sina.com.cn/s/blog_7243284f01012qqh.html)
