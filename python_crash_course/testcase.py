# -*- coding:utf-8 -*-
# authority by Nutter
# 《python编程：从入门到实践》第11章 测试代码

import sys
import os
import unittest

from python_crash_course.name_function import get_formatted_name, get_formatted_city

# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(r"D:\project\python\python-learning\python_crash_course"))))


class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """测试函数必须以test开头"""
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


class CityTestCase(unittest.TestCase):
    """测试name_function.py中的get_formatted_city方法"""

    def test_city_country(self):
        """能够正确地处理像Santiago, Chile这样的城市+国家显示方式吗？"""
        formatted_name = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """能够正确地处理像Santiago, Chile  - population=500000这样的城市+国家显示方式吗？"""
        formatted_name = get_formatted_city('santiago', 'chile', 500000)
        self.assertEqual(formatted_name, 'Santiago, Chile - Population=500000')
        # TypeError: can only concatenate str (not "int") to str 表示字符串只能拼接字符串，不能拼接int


# 缺少if __name__ == '__main__'无法运行test
if __name__ == '__main__':
    unittest.main()
