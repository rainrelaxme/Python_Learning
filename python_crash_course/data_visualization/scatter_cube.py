# -*- coding:utf-8 -*-
# authority by Nutter
# 《python编程：从入门到实践》第15章 数据可视化

# 15-1 立方 ：数字的三次方被称为其立方。请绘制一个图形，显示前5个整数的立方值，再绘制一个图形，显示前5000个整数的立方值。
# 15-2 彩色立方 ：给你前面绘制的立方图指定颜色映射。

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, cmap=plt.cm.Blues, s=20)

# 设置标题和标签
plt.title("Scatter cube", c=(0.8, 0, 0), fontsize=24)
plt.xlabel("Value", c="blue", fontsize=14 )
plt.ylabel("Cube of value", c="blue", fontsize=14)

# 设置取值范围
plt.axis([0, 100, 0, 1000000])

plt.savefig("Cube_plot.jpg", bbox_inches='tight')
