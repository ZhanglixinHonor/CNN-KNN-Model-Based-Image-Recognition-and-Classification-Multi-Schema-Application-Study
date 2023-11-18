"""
current project: BmOrFm_03          
current file: test                     
current @author: ilmare                  
you are using PyCharm             
this file create at 19:28 2021/8/1       
"""
import numpy as np
import matplotlib.pyplot as plt


def draw_loss():
    file_name = "E:/Users/zhang/lunwendaima/BmOrFm_0005/trainLog0"
    conV_name = ["Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ", "Ⅴ", "Ⅵ", "Ⅶ", "Ⅷ", "Ⅸ"]
    # 1 - Ⅰ、2 - Ⅱ、3 - Ⅲ、4 - Ⅳ、5 - Ⅴ、6 - Ⅵ、7 - Ⅶ、8 - Ⅷ、9 - Ⅸ
    for i in range(9):
        plt.figure()
        print(i)
        file_input = file_name + str(i+1) + ".log"
        print(file_input)
        (labelMat, dataMat) = np.loadtxt(fname=file_input, dtype=float, delimiter=',', usecols=(3, 5), unpack=True, skiprows=1)
        label_name = "Configuration " + conV_name[i]
        img_add = label_name + ".jpg"
        x = []
        y = []
        for i in range(0, len(dataMat)):
            x.append(labelMat[i])
            y.append(dataMat[i])


        plt.plot(x, y, 'r', label=label_name)
        # ‘’g‘’代表“green”,表示画出的曲线是绿色，“-”代表画的曲线是实线，可自行选择，label代表的是图例的名称，一般要在名称前面加一个u，如果名称是中文，会显示不出来，目前还不知道怎么解决。
        plt.legend()    #显示图例

        plt.xlabel("Iters")
        plt.ylabel("Train loss")
        plt.title("Train loss vs. Iters")

        plt.draw()
        plt.ylim(0.0, 0.4)

        plt.savefig(fname='./pic/'+img_add)
    plt.show()


if __name__ == '__main__':
    draw_loss()
    # conV_name = ["Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ", "Ⅴ", "Ⅵ", "Ⅶ", "Ⅷ", "Ⅸ"]
    # print(conV_name[0])