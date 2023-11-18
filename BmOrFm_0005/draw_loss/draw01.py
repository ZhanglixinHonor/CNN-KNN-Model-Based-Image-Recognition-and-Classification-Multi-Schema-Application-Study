"""
current project: BmOrFm_03          
current file: draw01                     
current @author: ilmare                  
you are using PyCharm             
this file create at 20:03 2021/7/31       
"""
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

import matplotlib.pyplot as plt
import pylab as pl
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

(labelMat, dataMat) = np.loadtxt("trainLog01.log", skiprows=1, dtype=float, delimiter=',', usecols=(3, 5), unpack=True)

# file=open('trainLog01.log')
# dataMat=[]
# labelMat=[]
# for line in file.readlines():
#     curLine=line.strip().split(",")
#     labelMat.append(float(curLine[3]))
#     dataMat.append(float(curLine[5]))
# file.close()

print(labelMat)
print(dataMat)

x = []
y = []
for i in range(0, len(dataMat), 20):
    x.append(labelMat[i])
    y.append(dataMat[i])

print(x)
print(y)


plt.plot(x, y, 'r', label="loss")
# ‘’g‘’代表“green”,表示画出的曲线是绿色，“-”代表画的曲线是实线，可自行选择，label代表的是图例的名称，一般要在名称前面加一个u，如果名称是中文，会显示不出来，目前还不知道怎么解决。
plt.legend()
#显示图例

plt.xlabel(u'iters')
plt.ylabel(u'loss')
plt.title('Compare loss for different models in training')

plt.draw()
plt.ylim(0.0, 0.5)
plt.show()

# 如何通过python画loss曲线
# https://blog.csdn.net/qq_32855463/article/details/86610098

# CNN入门+猫狗大战(Dogs vs. Cats)+PyTorch入门
# https://blog.csdn.net/l1076604169/article/details/92747124