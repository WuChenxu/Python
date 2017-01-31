import re
import urllib

file_name="./movie_quotes.txt"

def read_text():
    quotes = open(file_name)
    contents_of_file = quotes.read()
    print(contents_of_file)
    check_profanity(contents_of_file)
    
    quotes.close()

def check_profanity(text_to_check):
    print("create connection..")
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    print("connected...")
    output = connection.read()
    print(output)
    connection.close()


read_text() 
