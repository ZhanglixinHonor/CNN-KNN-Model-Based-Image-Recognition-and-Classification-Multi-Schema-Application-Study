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
y = [0.8922, 0.9412, 0.9118, 0.8110, 0.8343, 0.8235, 0.8333, 0.8135, 0.9020]

fig = plt.figure()
plt.bar(x, y, 0.8, color=['b', 'g', 'b', 'b', 'b', 'b', 'b', 'b', 'b'])

# plt.xlabel("Configuration")
plt.ylabel("Accuracy")
# plt.title("bar chart")
plt.ylim(0.5, 1.0)
plt.show()
# plt.savefig("after.jpg")