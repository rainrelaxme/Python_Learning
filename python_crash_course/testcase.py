# -*- coding:utf-8 -*-
# authority by Nutter
# 《python编程：从入门到实践》第11章 测试代码

import sys
import os
import unittest
import random

from python_crash_course.test_function import get_formatted_name, get_formatted_city
from python_crash_course.test_function import AnonymousSurvey, Employee


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


class TestAnonymousSurvey(unittest.TestCase):
    """测试AnonymousSurvey类："""

    def test_store_single_response(self):
        """测试单个答案会被妥善的存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)   # 断言方法之一，item在list中

    def test_store_multiple_responses(self):
        """测试多个答案是否会被妥善的存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


class TestAnonymousSurvey2(unittest.TestCase):
    """测试AnonymousSurvey类的另一种方案,采用setUp()方法"""

    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What language did you like best?"
        self.my_survey = AnonymousSurvey(question)  # 加上self.代表是类的属性，可以在类内部其它函数引用
        self.responses = ['Chinese', 'English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案是否会被妥善存储"""
        self.my_survey.store_response(self.response[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_multiple_responses(self):
        """测试多个答案是否会被妥善存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


class TestEmployee(unittest.TestCase):
    """测试员工"""

    def setUp(self):
        """创建一个员工对象和其涨薪方式"""
        first_name = 'shawn'
        second_name = 'zhu'
        salary = 10000
        self.person = Employee(first_name, second_name, salary)
        
    def test_give_default_raise(self):
        """测试涨薪方法默认5000"""
        self.person.give_raise()
        self.assertEqual(15000, self.person.salary)

    def test_give_custom_raise(self):
        """测试随机涨薪数值"""
        self.person.give_raise(random.uniform(1, 10000))


# 缺少if __name__ == '__main__'无法运行test
if __name__ == '__main__':
    unittest.main()
