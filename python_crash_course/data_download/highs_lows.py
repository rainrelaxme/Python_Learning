# -*- coding:utf-8 -*-
# authority by Nutter
# 《python编程：从入门到实践》第16章 下载数据

import csv

from matplotlib import pyplot as plt
from datetime import datetime

# filename = 'sitka_weather_07-2018_simple.csv'
filename = 'sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # # 输出csv文件全部内容，没有表头
    # content = []
    # for column in reader:
    #     content.append(column)
    # print(content)

    # 输出表头信息
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    # 输出最高气温列的内容
    dates, highs, lows = [], [], []
    for row in reader:
        # print(row, "\n", row[8])

        # 报错处理，其中有部分日期未记录最高气温和最低气温
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[8])
            low = int(row[9])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))

# 绘制两条线
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)

# 填充中间部分
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的样式
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate() # 使横坐标调整
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which='major', labelsize=16)
# plt.savefig("weather_show.jpg")   # 存储图片 需要放在show()前面
plt.show()

