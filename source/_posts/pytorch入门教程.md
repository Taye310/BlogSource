---
title: pytorch入门教程
date: 2018-11-19 21:02:00
tags:
    - pytorch
    - 深度学习
    - cifar-10
---

### 任务目标
对Cifar-10图像数据集，用卷积神经网络进行分类，统计正确率。
学会安装pytorch开源深度学习框架并调用它的接口。
直接采用pytorch针对Cifar-10数据集已训练好的网络模型，只做测试。

### 实验过程

**准备阶段**
开发环境：windows10+anaconda+vscode，python3.6，pytorch0.4.1。 
首先安装anaconda，内置的环境配置功能，Spyder、JupterNotebook工具都能提高学习和开发效率； 
因为要使用GPU加速训练，选择合适的CUDA版本进行安装，我使用的是9.2版本。 
根据自己的环境在pytorch官网查找对应的安装命令： 
	conda install pytorch cuda92 -c pytorch 
	pip3 install torchvision 

**图像分类**
Torchvision提供了数据集的下载API，可以很方便的下载Cifar-10数据集并分为训练集和测试集； 
成功载入数据后，开始搭建神经网络，定义神经网络的层次结构以及正向传递函数； 
初始化一个网络对象并载入GPU（使用CPU训练可以省略这个步骤）； 
下面定义训练函数，损失函数选择交叉熵损失函数，优化函数选择梯度下降算法，训练的每一次迭代中使用损失函数进行反向传递，优化器更新参数； 
下面进入测试阶段，统计10000张测试图片的正确率，统计每一类图片（1000张）的正确率。 

**Pytorch API**
Torchvision.datasets	数据集 
Torch.nn		神经网络模块 
Torch.optim	用于实现多种优化算法的包 

torch.utils.data.DataLoader	载入数据（需要注意的是该方法第四个参数决定是否使用多线程载入数据，而windows上的python对于多线程的支持与linux不同） 
nn.conv2d()	卷积层 
nn.maxpool2d()		池化层 
nn.zeropad2d()		填充边界 
nn.linear()			线性变化 
nn.CrossEntropyLoss()	交叉熵损失函数 
optim.SGD			梯度下降算法 
torch.max()			返回张量中最大的值 

**保存和载入模型**
保存模型 
torch.save(net.state_dict(), './MyTrainedModel/pretrained.pth') 
载入模型 
net.load_state_dict(torch.load('./MyTrainedModel/pretrained.pth')) 
net.eval() 