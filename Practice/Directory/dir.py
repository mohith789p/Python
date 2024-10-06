# have to create a demo.py file manually

import os
print(os.getcwd())  # return the present  working directory
print(os.getcwdb())  # return the present working directory as a bytes object
print(os.listdir())   # return a list containing the names of the entries in the directory given by path
os.chdir('D:\Desktop\Python\Practice\Directory')   # change the current working directory
os.mkdir('New Folder')    # create a new directory
print(os.listdir())  # return a list containing the names of the entries in the directory given by path after creating a new
os.rename('New Folder','File 01')   # rename a file or directory
os.rename('demo.py','trail.py')
print(os.listdir())   # return a list containing the names of the entries in the directory given by path after renaming
os.rmdir('File 01')    # remove a directory
print(os.listdir())   # return a list containing the names of the entries in the directory given by path after removing a
os.remove('trail.py')    # remove a file
print(os.listdir())   # return a list containing the names of the entries in the directory given by path after removing a