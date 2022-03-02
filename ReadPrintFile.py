#!/usr/bin/env python3
#Interacting with Files. Read a file and print the content 

import os

'''
cwd = os.getcwd() #get the current worlking director
files = os.listdir(cwd) #Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
'''

xmen_file = open('xmen_base.txt', 'r') #r means read

xmen_file.seek(0) #this enable you to seek at which position of the file. ) is the beginning
number_of_characters = len(xmen_file.read())
xmen_file.seek(0)
print(xmen_file.read())

print(f'File have {number_of_characters} number of characters')
xmen_file.close() #to close the file. Impt to close after using