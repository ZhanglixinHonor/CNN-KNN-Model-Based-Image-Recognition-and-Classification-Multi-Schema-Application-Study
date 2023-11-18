"""
current project: BmOrFm_04          
current file: draw_acc2                     
current @author: ilmare                  
you are using PyCharm             
this file create at 20:29 2021/8/8       
"""

# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ']
y = [0.9479, 0.9433, 0.9515, 0.8839, 0.9495, 0.9039, 0.9194, 0.9359, 0.9505]

fig = plt.figure()
plt.bar(x, y, 0.8, color=['b', 'b', 'g', 'b', 'b', 'b', 'b', 'b', 'b'])

# plt.xlabel("Configuration")
plt.ylabel("Accuracy")
# plt.title("bar chart")
plt.ylim(0.5, 1.0)
plt.show()
# plt.savefig("after.jpg")