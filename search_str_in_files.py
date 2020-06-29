# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Auther:zhaohs

''' 遍历某个文件夹下的所有txt，返回某个字符出现在哪个文件，并且出现的次数'''
import os

def f(file_path,s):
    '''
	:param file_path: Absolute path
    :param s: Searched string
	:return: Number of occurrences in each file
    '''
	dic={}
	for file in os.listdir(file_path):
		with open(os.path.join(file_path,file),'r') as f:
			lines=f.readlines()
			for line in lines:
				if s in line:
					if file in dic:
						dic[file]+=1
					else:dic[file]=1
	return dic



