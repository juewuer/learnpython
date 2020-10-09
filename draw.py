#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/13 23:20
# @Author  : Juewuer @ github.com
# @Site    : 
# @File    : draw.py
# @copyright: ksyun


import matplotlib.pyplot as plt

import mpl_toolkits

from mpl_toolkits.basemap import Basemap

plt.figure(figsize=(16,8))
m = mpl_toolkits.basemap.Basemap()
m.drawcoastlines()

plt.show()