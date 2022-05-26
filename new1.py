# -*- coding:utf-8 -*-
import os 

def find_prefix_of_path(path, file_list):
    
	
	files = os.listdir(path)
    for file_name in files:
        file_path = os.path.join(path, file_name)

        if os.path.isdir(file_path):
            find_prefix_of_path(file_path, file_list)
        elif os.path.isfile(file_path) and u'test' in file_name:
            file_list.append(file_path)
	

paths = u'D:\Project\Python'

file_list = []

find_prefix_of_path(paths, file_list)

print(file_list)