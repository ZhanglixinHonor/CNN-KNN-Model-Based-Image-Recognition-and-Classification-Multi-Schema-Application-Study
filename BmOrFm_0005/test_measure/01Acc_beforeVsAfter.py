"""
current project: BmOrFm_04          
current file: beforeVsAfter                     
current @author: ilmare                  
you are using PyCharm             
this file create at 20:44 2021/8/8       
"""

import numpy as np
import matplotlib.pyplot as plt

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
# 输入统计数据
x = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ']
# accuracy
# ACC  =================================================================================
y_before = [0.8922, 0.9412, 0.9118, 0.8110, 0.8343, 0.8235, 0.8333, 0.8135, 0.9020]
y_after = [0.9479, 0.9433, 0.9515, 0.8839, 0.9495, 0.9039, 0.9194, 0.9359, 0.9505]

bar_width = 0.4  # 条形宽度
index_before = np.arange(len(x))  # 男生条形图的横坐标
index_after = index_before + bar_width  # 女生条形图的横坐标

# 使用两次 bar 函数画出两组条形图
plt.bar(index_before, height=y_before, width=bar_width, color='b', label='Before')
plt.bar(index_after, height=y_after, width=bar_width, color='g', label='After')

plt.legend(loc="upper right")  # 显示图例
plt.xticks(index_before + bar_width / 2, x)  # 让横坐标轴刻度显示 x ， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel("Configuration")
plt.ylabel('accuracy')  # 纵坐标轴标题
plt.title('Data Augmentation (Before Vs After)')  # 图形标题
plt.draw()
plt.ylim(0.7, 1.0)
plt.savefig("01acc_beforeVsafter.jpg")
plt.show()
