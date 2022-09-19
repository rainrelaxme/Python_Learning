# -*- coding:utf-8 -*-
# authority by Nutter
# 《python编程：从入门到实践》第15章 数据可视化 15.4

import pygal

from die import Die

# 创建一个D6
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(value)
    frequencies.append(frequency)

# 对结果可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
# hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_labels = range(1, die.num_sides+1)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies[1::2])   # 切片
hist.render_to_file('die_visual.svg')
