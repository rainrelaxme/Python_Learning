# -*- coding:utf-8 -*-
# authority by Nutter
# 《python编程：从入门到实践》第11章 测试代码
# 学习处理文件，并处理异常

def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""

    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()


def get_formatted_city(city, country, population: int = ''):
    """城市和国家名"""

    if population:
        full_name = city + ', ' + country + ' - population=' + str(population)
    else:
        full_name = city + ', ' + country
    return full_name.title()


class AnonymousSurvey:
    """收集匿名调查问卷的答案"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查问卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)


class Employee:
    """用于存储职员信息，包括姓名、年薪、涨薪、显示薪酬功能"""

    def __init__(self, first_name, second_name, salary: float):
        """职员：名、姓、年薪"""
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary

    def give_raise(self, raise_money: float = 0):
        """给职员涨薪"""
        if raise_money:
            self.salary = self.salary + raise_money
        else:
            self.salary = self.salary + 5000
        return self.salary
