# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:16:36 2020

@author: iwill
"""

import numpy as np, pandas as pd

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.ticker as tic
from matplotlib.dates import DateFormatter

x = np.array(range(10))
y = np.array(range(10))

# フォントの種類とサイズを設定する。
plt.rcParams['font.size'] = 14
plt.rcParams['font.family'] = 'Times New Roman'
 
# 目盛を内側にする。
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
 
# グラフの上下左右に目盛線を付ける。
fig = plt.figure(figsize=(6, 4), dpi=50)
ax1 = fig.add_subplot(111)
ax1.yaxis.set_ticks_position('both')
ax1.xaxis.set_ticks_position('both')
 
# 軸のラベルを設定する。
ax1.set_xlabel('x')
ax1.set_ylabel('y')
 
# データプロットの準備。
#散布図
ax1.scatter(x, y, label='sample', lw=1, marker="o")
#折れ線グラフ
ax1.plot(x, y, label='fitted curve', lw=1)
 
# グラフを表示する。
#plt.xlabel("Ｘ軸", fontname="MS Gothic")
#plt.ylabel("Ｙ軸（二乗値）", fontname="MS Gothic")
plt.title('title', fontname="MS Gothic")
plt.savefig("img.png")
plt.close()