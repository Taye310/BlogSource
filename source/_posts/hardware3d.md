---
title: hardware3d
date: 2020-04-14 15:49:36
tags: 
    - Dx12
    - WindowsApp
    - COM
---

# Hardware 3D

COM：
<iframe width="560" height="315" src="https://www.youtube.com/embed/Ut5zYcDKGwk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

framebuffer: 双重缓冲是一个画（用户操作），一个已经画好的传输给显示器做显示，一个称为front，另一个称为back buffer。  
还可以有多重缓冲，缓冲层数越多，会导致画面延迟加重，但是更加连贯顺滑。原因是有时候front没花完，显示器已经逐像素扫描完一个frame，显示器就得等front buffer。  
vsync：防tearing，就是等显示器一个frame完成再载入下一个buffer  

constant buffer: 用来存变换矩阵，目的是用shader控制图形旋转，而不是改变vertices的坐标  

shader中对于matric的修饰词 row_major会降低速度  

DirectX Math： SIMD(single instruction multiple data)  

depth buffer shares memory with stencil buffer(模板缓冲): masking like mirror,portals. depth buffer optimized for depth  

direct toolkit for loading texture会省掉很多工作，所以这里用了GDI+  

[hlsl intrinsic functions](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-intrinsic-functions)  

[attenuation](http://wiki.ogre3d.org/-Point+Light+Attenuation)

## imGUI

使用方法：根目录的header和source文件 + examples里的对应平台文件（例如dx11+win32的四个文件）  

# 3D Fundamental

rasterization rule: left-top rule;

# 《Unity shader 入门精要》

[NDC与视锥体剪裁](https://www.zhihu.com/question/304277310)：视锥体剪裁在cpu中进行，gpu流水线中还有一次culling，是按NDC空间进行剪裁（超出-1到1就裁剪，dx的z-axis是0-1）。这两次剪裁功能相似，第一次的目的是减轻gpu负担。  

模板测试（stencil test）：可以理解为深度测试中的深度这个概念有开发者人为设定。  

blend（混合）/output merger

early-z

# Unreal source code review

