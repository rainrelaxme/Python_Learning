# -*- coding:utf-8 -*-
# authority by Nutter
# 《python编程：从入门到实践》第15章 数据可视化

import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
    """随机漫步"""

    def __init__(self, num_points=5000):
        self.num_points = num_points
