---
title: Games101图形学入门课程
date: 2020-09-03 14:42:22
mathjax: true
tags:
    - 图形学
    - 线上课程
---

# Games-cn 101图形学课程

[视频链接](https://www.bilibili.com/video/BV1X7411F744)  
[官网链接](http://games-cn.org/intro-graphics/)

## P4 Transformation

旋转矩阵是正交矩阵，正交矩阵的逆=正交矩阵的转置  

TODO 投影变换推导（透视投影，正交投影，弱透视投影）
[参考资料](https://zhuanlan.zhihu.com/p/158856632)

## p6 Rasterization 2

走样的本质：Sample（采样）的本质是离散化表示一个时域图像，离散化表示时域图像在频域上看是对频域图像的不断复制。当分辨率低，采样间隔大时，频域空间的间隔反而小，这会导致重复的频域图像间有重叠，结果就是导致走样。


## p7 Shading 1

Lambertian(Diffuse) Shading independent of view direction
$$ L_{d} = k_{d}(I/r^{2})max(0,n·l) $$
[视频连接59:00](https://www.bilibili.com/video/BV1X7411F744?p=7)

## p8 Shading 2

Specular Term(Blinn-Phong)
$$ h = bisector(v,I) \\
     = {v+l\over \parallel v+l \parallel} $$
$$ L_{s} = k_{s}(I/r^{2})max(0,cos\alpha) \\
         = k_{s}(I/r^{2})max(0,n·h) $$
> 高光和观察点（相机）位置有关系，越光滑的平面越接近镜面反射，反之会形成围绕反射方向的一个反射区间，Blinn-Phong通过引入半程向量，比较半程向量和法线是否接近（blinn-phong）来代替出射方向和视角方向是否接近（phong），因为出射方向不好算  

高光项会加个指数p，来控制高光区域的大小
$$ L_{s} = k_{s}(I/r^{2})max(0,n·h)^{p} $$


Ambient Term在blinn-phong中就是个常数项，以后会接触GI，比较复杂  

shading频率：Flat、Gouraud、Phong分别对应逐面、逐顶点、逐像素  

## p9 Shading 3

Barycentric Coordinates（重心坐标）：
$$ \alpha + \beta + \gamma = 1 $$
$$ \alpha A + \beta B + \gamma C = (x,y) $$
ABC三点平面内的任意点P(x,y)可以用上式表达，当$\alpha \beta \gamma$ 均 >0 时，点P在三角形内部  
$\alpha \beta \gamma$ 的值可以[通过三角想面积求得15:00](https://www.bilibili.com/video/BV1X7411F744?p=9)  

处理摩尔纹：mipmap  
计算Mipmap Level D： $D = log_{2}L$  
三线性插值：一个插值是level与level间的，一个是纹理相邻像素间的  

Overblur：用各向异性过滤 == Ripmap，就是生成横竖拉伸的，大小为原来纹理三倍的纹理贴图  

