---
title: deeplearning.ai
date: 2018-12-18 10:08:59
tags:
    - Andrew Ng
    - Deeplearning
    - AI
---

# Improving Deep Neural Networks: Hyperparameter tuning, Regularization and Optimization

train/dev/test data set 在过去通常 60/20/20% 的比例，总样本数在10,000  
大数据时代通常在 98/1/1 或者后两个更小的比例，总样本在1,000,000  
  
high bias&high variance  
判断网络模型高偏差还是高方差还是两者都有的方法：  
    训练集上的错误率过高就是高偏差（例：人错误率，也称base error 1%，模型训练集上错误率15%，模型在开发集上错误率16%）  
    开发集上的错误率比训练集上的错误率高过多是高方差（例：人错误率14%，模型训练集上错误率15%，模型在开发集上错误率30%）  
  
高偏差-->更大的网络  
高方差-->更多的数据-->可能导致偏差变高-->高偏差  

## Regularization正则化
为的是避免过拟合  
L2 正则化 最常用 也被称为weight decay  
L1 正则化  
**实际上，可以将Logistic Regression看做是仅含有一个神经元的单层的神经网络！**  
正则化是如何避免overfitting的，换句话说怎么减小方差（variance）的？  
使得w变小-->z变小-->导致激活函数所取范围接近线性-->避免overfitting，即避免高维非线性  
  
What is L2-regularization actually doing?:  

L2-regularization relies on the assumption that a model with small weights is simpler than a model with large weights. Thus, by penalizing the square values of the weights in the cost function you drive all the weights to smaller values. It becomes too costly for the cost to have large weights! This leads to a smoother model in which the output changes more slowly as the input changes.   
  
Dropput 正则化：  
inverted dropout///keep-prob 一层的unit个数越多过拟合的可能越大，所以keep probability可以设置的小一些  
dropout在计算机视觉中经常用 因为输入是像素会非常多  
  
对训练数据，例如图片进行翻转可以double训练数据数量 还有旋转、剪裁 几乎没有花费  
Early stopping  
normalizing training sets 为的是加速梯度下降算法，增加优化的步长  
如果网络层数非常大，会导致梯度下降传递的值指数型增大或减小，为避免，应当合理的初始化weight，使其接近1  
  
12.27  
gradient checking 反向传递函数容易有bug又不易察觉，梯度检查就是检查导数算的对不对，可以增加对反向传递函数实现的正确性的信心  
Debugging: Gradient Checking [参考资料](http://ufldl.stanford.edu/tutorial/supervised/DebuggingGradientChecking/)  
  
