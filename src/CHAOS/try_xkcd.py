#!/usr/local/anaconda3/envs/py39torch118/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/8 19:20
# @Author  : Berlin Wong
# @File    : try_xkcd.py
# @Software: PyCharml

import matplotlib.pyplot as plt

with plt.xkcd():
    plt.bar([1, 2, 3], [1, 2, 3])
    plt.title('test')
    plt.show()
