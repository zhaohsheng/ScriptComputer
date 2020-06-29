# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Auther:zhaohs

''' 遍历某个文件夹下的所有txt，返回某个字符出现在哪个文件，并且出现的次数'''
import os

def f(file_path,s):

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


file_path="C:\\Users\\zhaoh\\Desktop\\测试\\测试学习内容\\1"
str='2'
print(f(file_path,str))
