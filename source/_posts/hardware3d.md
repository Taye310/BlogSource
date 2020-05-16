---
title: hardware3d
date: 2020-04-14 15:49:36
tags: 
    - Dx12
    - WindowsApp
    - COM
---

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

### imGUI

 