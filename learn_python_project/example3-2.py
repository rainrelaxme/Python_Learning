#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sqlite3
#打开数据库
def opendb():
    conn = sqlite3.connect("D:\mydb\mydb.db")
    cur = conn.execute("create table if not exists tongxinlu(usernum integer primary key, username varchar(128), password varchar(128), address varchar(125), telnum varchar(128))")
    return cur, conn


#查询全部信息
def showalldb():
	print("------------------处理后的数据------------------")
	hel = opendb()
	cur = hel[1].cursor()
	cur.execute("select * from tongxinlu")
	res = cur.fetchall()
	for line in res:
		for h in line:
			print(h)
		print
	cur.close()
	
#输入信息
def into():
    usernum = input("请输入学号: ")
    uesrname = input("请输入姓名：")
    password = input("请输入密码：")
    address = input("请输入地址：")
    telnum = input("请输入联系电话：")
    return usernum, username, password, address, telnum
	
#往数据库中添加内容
def adddb():
	welcome = "------------------欢迎使用添加数据功能------------------"
	print(welcome)
	person = into()
	hel = opendb()
	hel[1].execute("insert into tongxinlu(usernum, username, password, address,telnum)	values(?,?,?,?,?)", (person[0], person[1], person[2], person[3], person[4]))
	hel[1].commit()
	print("-----------------------恭喜你，数据添加成功-----------------------")
	showalldb()
	hel[1].close()
	
#删除数据库中的内容
def deldb():
	welcome = "------------------欢迎使用删除数据库功能------------------"
	print(welcome)
	delchoice = input("请输入想要删除的学号：")
	hel = opendb()
	hel[1].execute("delete from tongxinlu where usernum = " + delchoice)
	hel[1].commit()
	print("------------------恭喜你，数据删除成功------------------")
	showalldb()
	hel[1].close()
	
#修改数据库的内容
def alter():
	welcome = "------------------欢迎使用修改数据库功能------------------"
	print(welcome)
	changechoice = input("请输入想要修改的学生的学号：")
	hel = opendb()
	person = into()
	hel[1].execute("upadte tongxinlu set usenum=?,username=?,password=?,address=?,telnum=? where usenum= " + changechoice,(person[0],person[1],person[2],person[3],person[4]))
	hel[1].commit()
	showalldb()
	hel[1].close()
			
#查询数据
def searchdb():
	welcome = "------------------欢迎使用查询数据库功能------------------"
	print(welcome)
	choice = input("请输入要查询的学生的学号：")
	hel = opendb()
	cur = hel[1].cursor()
	cur.execute("select * from tongxinlu where uesrnum="+choice)
	hel[1].commit()
	print("------------------恭喜你，想要查找的数据如下------------------")
	for row in cur:
		print(row[0],row[1], row[2], row[3], row[4])
	cur.close()
	hel[1].close()
	
#是否继续
def conti():
	choice = input("是否继续？(y or n): ")
	if choice == 'y':
		a=1
	else:
		a=0
	return a 
	
if __name__=="__main__":
	flag=1
	while flag:
		welcome = "------------------欢迎使用查询数据库功能------------------"
		print(welcome)
		choiceshow="""
		请选择您的进一步选择：
		（添加）往数据库中添加内容
		（删除）删除数据库中的内容
		（修改）修改数据库的内容
		（查询）查询数据库的内容
		选择您想要进行的操作：
		"""
		choice = input(choiceshow)
		if choice == "添加":
			adddb()
			conti(flag)
		elif choice == "删除":
			deldb()
			conti(flag)
		elif choice == "修改":
			alter()
			conti(flag)
		elif choice == "查询":
			searchdb()
			conti(flag)
		else:
			print("您输入错误，请重新输入")
