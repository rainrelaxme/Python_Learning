# -*- coding:utf-8 -*-
# authority by Nutter
# 《python编程：从入门到实践》第15章 数据可视化

import matplotlib.pyplot as plt

"""如何快速开始一个新行：在当前行任意位置，使用shif+Enter在下面新建一行，使用ctrl+alt+Enter在上面新建一行"""

x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]

# edgecolors表明数据点轮廓是否存在
# c表示点的颜色，采用rgb时，值越接近0，指定的颜色越深，越接近1，指定的颜色越浅 # c=(0.8, 0, 0)
# 颜色影射，使用cmap使用某种颜色的映射，将值较小的显示未浅色，值较大的显示为深色
plt.scatter(x_value, y_value, edgecolors='none', cmap=plt.cm.Blues, s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Scatter Squares", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# plt.show()
# 保存图片
plt.savefig('square_plot.png', bbox_inches='tight')



