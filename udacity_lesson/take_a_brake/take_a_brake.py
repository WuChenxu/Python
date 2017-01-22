import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program starts at "+time.ctime())
while (break_count < total_breaks):
	time.sleep(10)
	print("[%d]time to break, now is[%s]." %(break_count, time.ctime()))
	webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
	break_count = break_count + 1

print("This programm ends at"+time.ctime())
