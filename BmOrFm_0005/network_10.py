import torch
import torch.nn as nn
import torch.utils.data
import torch.nn.functional as F


class Net(nn.Module):                                       # 新建一个网络类，就是需要搭建的网络，必须继承PyTorch的nn.Module父类
    def __init__(self):                                     # 构造函数，用于设定网络层
        super(Net, self).__init__()                         # 标准语句
        self.conv1 = torch.nn.Conv2d(3, 16, 3, padding=1)   # 第一个卷积层，输入通道数3 ，输出通道数16，卷积核大小3×3，padding大小1，其他参数默认
        self.conv2 = torch.nn.Conv2d(16, 16, 3, padding=1)  # 第二个卷积层，输入通道数16，输出通道数16，卷积核大小3×3，padding大小1，其他参数默认
        self.conv3 = torch.nn.Conv2d(16, 16, 3, padding=1)  # 第三个卷积层，输入通道数16，输出通道数16，卷积核大小3×3，padding大小1，其他参数默认
        self.conv4 = torch.nn.Conv2d(16, 16, 3, padding=1)  # 第四个卷积层，输入通道数16，输出通道数16，卷积核大小3×3，padding大小1，其他参数默认

        # self.fc1 = nn.Linear(100*100*16, 128)               # 第一个全连层，线性连接，输入节点数100*100*16，输出节点数128
        # self.fc1 = nn.Linear(50*50*16, 128)                 # 第一个全连层，线性连接，输入节点数50×50×16，输出节点数128
        self.fc1 = nn.Linear(25*25*16, 128)                 # 第一个全连层，线性连接，输入节点数25*25*16，输出节点数128
        self.fc2 = nn.Linear(128, 64)                       # 第二个全连层，线性连接，输入节点数128，输出节点数64
        self.fc3 = nn.Linear(64, 32)                        # 第三个全连层，线性连接，输入节点数128，输出节点数64
        self.fc4 = nn.Linear(32, 16)                         # 第四个全连层，线性连接，输入节点数64，输出节点数2
        self.fc5 = nn.Linear(16, 2)                         # 第四个全连层，线性连接，输入节点数64，输出节点数2

    def forward(self, x):                   # 重写父类forward方法，即前向计算，通过该方法获取网络输入数据后的输出值
        x = self.conv1(x)                   # 第一次卷积
        x = F.relu(x)                       # 第一次卷积结果经过ReLU激活函数处理
        x = F.max_pool2d(x, 2)              # 第一次池化，池化大小2×2，方式Max pooling

        x = self.conv2(x)                   # 第二次卷积
        x = F.relu(x)                       # 第二次卷积结果经过ReLU激活函数处理
        x = F.max_pool2d(x, 2)              # 第二次池化，池化大小2×2，方式Max pooling

        x = self.conv3(x)                   # 第三次卷积
        x = F.relu(x)                       # 第三次卷积结果经过ReLU激活函数处理
        x = F.max_pool2d(x, 2)              # 第三次池化，池化大小2×2，方式Max pooling
   
        x = self.conv3(x)                   # 第四次卷积
        x = F.relu(x)                       # 第四次卷积结果经过ReLU激活函数处理
        x = F.max_pool2d(x, 2)              # 第四次池化，池化大小2×2，方式Max pooling
        
        x = x.view(x.size()[0], -1)         # 由于全连层输入的是一维张量，因此需要对输入的[100*100*16]或[50×50×16]或[25*25*16]格式数据排列成[160000×1][40000×1][10000×1]形式
        x = F.relu(self.fc1(x))             # 第一次全连，ReLU激活
        x = F.relu(self.fc2(x))             # 第二次全连，ReLU激活
        x = F.relu(self.fc3(x))             # 第三次全连，ReLU激活
        y = self.fc4(x)                     # 第四次激活，ReLU激活

        return y

