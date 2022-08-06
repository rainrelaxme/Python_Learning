# -*- coding:utf-8 -*-
# authority by Nutter

import sys
import os
import unittest

from python_crash_course.test_function import get_formatted_name

# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(r"D:\project\python\python-learning\python_crash_course"))))


name = get_formatted_name('a', 'b', 'c')
print(name)

