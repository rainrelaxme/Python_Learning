# -*- coding:utf-8 -*-
# authority by Nutter
# 《python编程：从入门到实践》第15章 数据可视化 15.4

# import pygal
#
# from die import Die
#
# # 创建两个D6骰子
# die_1 = Die()
# die_2 = Die()
#
# # 掷骰子多次，并将结果存储到一个列表中
# results = []
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
#
# # 分析结果
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
#
# # 可视化结果
# hist = pygal.Bar()
#
# hist.title = "Results of rolling two D6 dice 1000 times."
# hist.x_labels = range(2, max_result+1)  # range(a,b)在b就停止，b不包含在内
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"
#
# hist.add('D6+D6', frequencies)
# hist.render_to_file('dice_visual.svg')


# 使用matplotlib模拟掷骰子
import matplotlib.pyplot as plt

from die import Die

# 创建一个D6
die = Die()

# 掷几次骰子
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
plt.plot(list(range(1, die.num_sides+1)), frequencies)
plt.title("Roll one die using matplotlib", fontsize=24)
plt.xlabel("Result")
plt.ylabel("Frequency of Result")

plt.show()