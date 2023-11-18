from getdata import DogsVSCatsDataset as DVCD
from model_08.network_08 import Net
import torch
from torch.autograd import Variable
import numpy as np
import torch.nn.functional as F
import torch.nn as nn
import matplotlib.pyplot as plt
from PIL import Image
import random
import os
import getdata

dataset_dir = './data/test/'                    # 数据集路径
model_file = './model/model08/model.pth'                # 模型保存路径
N = 17


# # old version
# def test():
#
#     model = Net()                                       # 实例化一个网络
#     model.cuda()                                        # 送入GPU，利用GPU计算
#     model = nn.DataParallel(model)
#     model.load_state_dict(torch.load(model_file))       # 加载训练好的模型参数
#     model.eval()                                        # 设定为评估模式，即计算过程中不要dropout
#
#     datafile = DVCD('test', dataset_dir)                # 实例化一个数据集
#     print('Dataset loaded! length of train set is {0}'.format(len(datafile)))
#
#     index = np.random.randint(0, datafile.data_size, 1)[0]      # 获取一个随机数，即随机从数据集中获取一个测试图片
#     img = datafile.__getitem__(index)                           # 获取一个图像
#     img = img.unsqueeze(0)                                      # 因为网络的输入是一个4维Tensor，3维数据，1维样本大小，所以直接获取的图像数据需要增加1个维度
#     img = Variable(img).cuda()                                  # 将数据放置在PyTorch的Variable节点中，并送入GPU中作为网络计算起点
#     print(img)
#     out = model(img)                                            # 网路前向计算，输出图片属于猫或狗的概率，第一列维猫的概率，第二列为狗的概率
#     out = F.softmax(out, dim=1)                                        # 采用SoftMax方法将输出的2个输出值调整至[0.0, 1.0],两者和为1
#     print(out)                      # 输出该图像属于猫或狗的概率
#     if out[0, 0] > out[0, 1]:                   # 猫的概率大于狗
#         print('the image is a cat')
#     else:                                       # 猫的概率小于狗
#         print('the image is a dog')
#
#     img = Image.open(datafile.list_img[index])      # 打开测试的图片
#     plt.figure('image')                             # 利用matplotlib库显示图片
#     plt.imshow(img)
#     plt.show()


# new version
def test():
    torch.cuda.empty_cache()
    testLog = open('testLog08.log', mode='a', encoding='utf-8')
    mean_rate = []
    for i in range(3):
        # setting model
        model = Net()                                       # 实例化一个网络
        model.cuda()                                        # 送入GPU，利用GPU计算
        model = nn.DataParallel(model)
        model.load_state_dict(torch.load(model_file))       # 加载训练好的模型参数
        model.eval()                                        # 设定为评估模式，即计算过程中不要dropout

        # get data
        files = random.sample(os.listdir(dataset_dir), N)   # 随机获取N个测试图像
        # files = os.listdir(dataset_dir)  # 随机获取N个测试图像

        imgs = []           # img
        imgs_data = []      # img data
        imgs_label = []     # img label
        for file in files:
            img = Image.open(dataset_dir + file)            # 打开图像
            img_data = getdata.dataTransform(img)           # 转换成torch tensor数据

            imgs.append(img)                                # 图像list
            imgs_data.append(img_data)                      # tensor list
            name = file.split(sep='.')
            # print(name)
            imgs_label.append(name[0])
            # print(imgs_label)
        imgs_data = torch.stack(imgs_data)                  # tensor list合成一个4D tensor
        print(imgs_label)

        # calculation
        out = model(imgs_data)                              # 对每个图像进行网络计算
        out = F.softmax(out, dim=1)                         # 输出概率化
        out = out.data.cpu().numpy()                        # 转成numpy数据

        error = 0
        rate = []
        # print(results)         显示结果
        # TP、True Positive 真阳性：预测为正，实际也为正
        # FP、False Positive 假阳性：预测为正，实际为负
        # FN、False Negative 假阴性：预测与负、实际为正
        # TN、True Negative 真阴性：预测为负、实际也为负。
        TP = 0
        FP = 0
        FN = 0
        TN = 0
        for idx in range(N):
            # plt.figure()
            print(imgs_label[idx])
            if out[idx, 0] > out[idx, 1]:
                # plt.suptitle('bm:{:.1%},fm:{:.1%}'.format(out[idx, 0], out[idx, 1]))
                if imgs_label[idx] == "fm":
                    error = error + 1
                    FN += 1
                    print(idx, 'bm:{:.5%},\t\tfm:{:.5%}'.format(out[idx, 0], out[idx, 1]), '\twrong!!!')
                    # print(idx, 'bm:{:.5%},\t\tfm:{:.5%}'.format(out[idx, 0], out[idx, 1]), '\twrong!!!', file=testLog)
                else:
                    TP += 1
                    print(idx, 'bm:{:.5%},\t\tfm:{:.5%}'.format(out[idx, 0], out[idx, 1]), '\tright')
                    # print(idx, 'bm:{:.5%},\t\tfm:{:.5%}'.format(out[idx, 0], out[idx, 1]), '\tright', file=testLog)
                    rate.append(out[idx, 0])
            else:
                # plt.suptitle('fm:{:.1%},bm:{:.1%}'.format(out[idx, 1], out[idx, 0]))
                if imgs_label[idx] == "bm":
                    error = error + 1
                    FP += 1
                    print(idx, 'fm:{:.5%},\t\tbm:{:.5%}'.format(out[idx, 1], out[idx, 0]), '\twrong!!!')
                    # print(idx, 'fm:{:.5%},\t\tbm:{:.5%}'.format(out[idx, 1], out[idx, 0]), '\twrong!!!', file=testLog)
                else:
                    TN += 1
                    print(idx, 'fm:{:.5%},\t\tbm:{:.5%}'.format(out[idx, 1], out[idx, 0]), '\tright')
                    # print(idx, 'fm:{:.5%},\t\tbm:{:.5%}'.format(out[idx, 1], out[idx, 0]), '\tright', file=testLog)
                    rate.append(out[idx, 1])
        #     plt.imshow(imgs[idx])
        # plt.show()
        print('acc_rate: ', rate)
        print(np.mean(rate))
        # print(error / N)
        print('error_rate: {:.5%}'.format(error/N))
        mean_rate.append(np.mean(rate))

        print('mean_rate: ', mean_rate)
        print(np.mean(mean_rate))
        print("TP: ", TP, ',\tFP: ', FP, ',\tTN: ', TN, ',\tFN: ', FN)
        #############################################################################
        # print('acc_rate: ', rate, file=testLog)
        # print(np.mean(rate), file=testLog)
        # # print(error / N)
        # print('error_rate: {:.5%}'.format(error/N), file=testLog)
        # mean_rate.append(np.mean(rate))
        #
        # print('mean_rate: ', mean_rate, file=testLog)
        # print(np.mean(mean_rate), file=testLog)
        print("TP,", TP, ',FP,', FP, ',TN,', TN, ',FN,', FN, file=testLog)
    testLog.close()
    # import pandas as pd
    # file = pd.read_csv('./data/submit_example.csv')
    # print(file.loc[1, 'label'] == 'cat')
    # error = 0
# 猫的概率：out[idx, 0]  狗的概率：out[idx, 1]
#     for idx in range(N):
#         print(idx)
#         print(imgs_label[idx])
#         a = int(imgs_label[idx])
#         print(file.loc[a, 'label'])
#         plt.figure()
#         if out[idx, 0] > out[idx, 1]:
#             plt.suptitle('cat:{:.1%},dog:{:.1%}'.format(out[idx, 0], out[idx, 1]))
#             if file.loc[a, 'label'] != 'cat':
#                 error += 1
#         else:
#             plt.suptitle('dog:{:.1%},cat:{:.1%}'.format(out[idx, 1], out[idx, 0]))
#             if file.loc[a, 'label'] != 'dog':
#                 error += 1
#         plt.imshow(imgs[idx])
#     plt.show()
#     print(error)
#     print("error: ", error/N)


if __name__ == '__main__':
    torch.cuda.empty_cache()
    test()
