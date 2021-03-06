#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 23:28
# @Author  : Juewuer @ github.com
# @Site    : 
# @File    : sample1.py
# @copyright: ksyun

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['savefig.facecolor'] = "0.8"


def example_plot(ax, fontsize=12):
    ax.plot([1, 2])

    ax.locator_params(nbins=3)
    ax.set_xlabel('x-label', fontsize=fontsize)
    ax.set_ylabel('y-label', fontsize=fontsize)
    ax.set_title('Title', fontsize=fontsize)

plt.close('all')
fig, ax = plt.subplots()
example_plot(ax, fontsize=24)