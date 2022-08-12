# -*- coding:utf-8 -*-
# authority by Nutter
# 《python编程：从入门到实践》第15章 数据可视化

import matplotlib.pyplot as plt


# 绘制点线图
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]     # 默认对应的x轴是从0开始
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()

# import matplotlib.pyplot as plt

# 绘制散点图
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=100)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()


import matplotlib.pyplot as plt

# 绘制散点图方法二
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=100)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的刻度范围,设置x轴y轴的范围
plt.axis(1, 1100, 0, 110000)

plt.show()