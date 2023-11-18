"""
current project: BmOrFm_04          
current file: draw——acc                     
current @author: ilmare                  
you are using PyCharm             
this file create at 20:09 2021/8/8       
"""
import matplotlib.pyplot as plt
import numpy as np

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 输入统计数据
x = ('Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ')
y = [0.9479, 0.9433, 0.9515, 0.8839, 0.9495, 0.9039, 0.9194, 0.9359, 0.9505]

bar_width = 0.8  # 条形宽度
index_male = np.arange(len(x))  # 男生条形图的横坐标

# 使用两次 bar 函数画出两组条形图
# plt.bar(index_male, height=y, width=bar_width, color='b', label='Configuration')
plt.bar(x, y)

plt.legend()  # 显示图例
# plt.xticks(index_male, x)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.ylabel('ACC')  # 纵坐标轴标题
plt.title('购买饮用水情况的调查结果')  # 图形标题
plt.ylim(0.5, 1.0)
plt.show()