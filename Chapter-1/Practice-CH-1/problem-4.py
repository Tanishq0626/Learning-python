# write a python program to print the contenta of a directory using os module 
import os

path = "C:/Users/TANISHQ/Documents"

files = os.listdir(path)

for item in files:
    print(item)
    