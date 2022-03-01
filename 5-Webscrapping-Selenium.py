
import os

#code on how to  make a directory and print it

keyword = 'Arteta'
path = os.getcwd()
path = os.path.join(path, keyword + "_pics")

os.mkdir(path)
print(path)