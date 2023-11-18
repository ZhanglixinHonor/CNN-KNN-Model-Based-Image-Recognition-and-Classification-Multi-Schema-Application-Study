"""
current project: BmOrFm_04          
current file: 02Sen_beforeVsAfter.py
current @author: ilmare                  
you are using PyCharm             
this file create at 21:37 2021/8/13       
"""
import matplotlib.pyplot as plt
import numpy as np

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
# 输入统计数据
x = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ']
# Matthews correlation coefficient
# MCC  =================================================================================
y_before = [0.7900, 0.8703, 0.8107, 0.6263, 0.7240, 0.6856, 0.6945, 0.7763, 0.8012]
y_after = [0.8966, 0.8701, 0.9036, 0.7853, 0.9000, 0.8163, 0.8486, 0.8751, 0.9008]

bar_width = 0.4  # 条形宽度
index_before = np.arange(len(x))  # 男生条形图的横坐标
index_after = index_before + bar_width  # 女生条形图的横坐标

# 使用两次 bar 函数画出两组条形图
plt.bar(index_before, height=y_before, width=bar_width, color='b', label='Before')
plt.bar(index_after, height=y_after, width=bar_width, color='g', label='After')

plt.legend(loc="upper right")  # 显示图例
plt.xticks(index_before + bar_width / 2, x)  # 让横坐标轴刻度显示 x ， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel("Configuration")
plt.ylabel('Matthews correlation coefficient')  # 纵坐标轴标题
plt.title('Data Augmentation (Before Vs After)')  # 图形标题
plt.draw()
plt.ylim(0.6, 1.0)
plt.savefig("01Matthews correlation coefficient_beforeVsafter2.jpg")
plt.show()
