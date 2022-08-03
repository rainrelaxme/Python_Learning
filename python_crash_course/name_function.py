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
