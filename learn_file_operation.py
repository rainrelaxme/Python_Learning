# -*- coding:utf-8 -*-
# 《python编程：从入门到实践》第10章 文件和异常
# 学习处理文件，并处理异常
from os import close

filename = 'test.txt'

# 读取文件
# 路径，在windows中用反斜杠，在linux和OS x中用斜杠
with open(filename) as file_object:  # open()打开文件
    # with可以在访问文件之后关闭它，也可以用open()和close()，但是只会在close时才关闭，如果调试未执行到close，会导致文件未妥善处理
    # open()仅在with代码块中使用，如果要给别的地方用，存储下来
    contents = file_object.read()
    print(contents.rstrip())    # .rstrip()用于删除末尾的空白
# 打印到一行中
message_string = ''
for line in contents:    # 此处已被关闭，无法读取内容，
    message_string += line.strip()   # 相较rstrip，strip可以去除前面的空格
m_replace = message_string.replace('i', 'I')    # 并不会真正替换
print(message_string)
print(m_replace)
print(len(message_string))   # 长度

new_file = open(filename)
contents = new_file.read()
print(contents.rstrip())    # .rstrip()用于删除末尾的空白
# 打印每一行
for line in file_object:
    print(line)
close(filename)

# 写文件
# 可指定读取模式 （'r' ）、写入模式 （'w' ）、附加模式 （'a' ）或让你能够读取和写入文件的模式（'r+' ）
"""
如果你省略了模式实参，Python将以默认的只读模式打开文件。
如果你要写入的文件不存在，函数open() 将自动创建它。
然而，以写入（'w' ）模式打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件。
"""
filename2 = 'test.txt'
with open(filename2, 'w') as file_object:
    file_object.write("I love programming.")

# 写入多行
with open(filename2, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 附加到文件
with open(filename2, 'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")