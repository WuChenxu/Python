all:
	gcc c_func.c -shared -fPIC -o c_func_dy.so
	python call_c_func.py 
	python python_func.py 

clean:
	rm -rf *.a *.so *.o
