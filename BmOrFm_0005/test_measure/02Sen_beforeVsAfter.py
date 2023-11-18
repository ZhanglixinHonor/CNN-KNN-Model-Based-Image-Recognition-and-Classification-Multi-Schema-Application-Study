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
# sensitivity
# Sen  =================================================================================
y_before = [0.9421, 0.9381, 0.8936, 0.7131, 0.7755, 0.7338, 0.8128, 0.9167, 0.8569]
y_after = [0.9315, 0.9157, 0.9581, 0.8293, 0.9716, 0.8632, 0.8868, 0.9647, 0.9543]

bar_width = 0.4  # 条形宽度
index_before = np.arange(len(x))  # 男生条形图的横坐标
index_after = index_before + bar_width  # 女生条形图的横坐标

# 使用两次 bar 函数画出两组条形图
plt.bar(index_before, height=y_before, width=bar_width, color='b', label='Before')
plt.bar(index_after, height=y_after, width=bar_width, color='g', label='After')

plt.legend(loc="upper right")  # 显示图例
plt.xticks(index_before + bar_width / 2, x)  # 让横坐标轴刻度显示 x ， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel("Configuration")
plt.ylabel('sensitivity')  # 纵坐标轴标题
plt.title('Data Augmentation (Before Vs After)')  # 图形标题
plt.draw()
plt.ylim(0.7, 1.0)
plt.savefig("01sen_beforeVsafter.jpg")
plt.show()
