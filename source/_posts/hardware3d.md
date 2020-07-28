---
title: 可编程渲染管线
date: 2020-04-14 15:49:36
mathjax: true
tags: 
    - Dx12
    - WindowsApp
    - COM
    - Shader
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

## 概念合集

[NDC与视锥体剪裁](https://www.zhihu.com/question/304277310)：视锥体剪裁在cpu中进行，gpu流水线中还有一次culling，是按NDC空间进行剪裁（超出-1到1就裁剪，dx的z-axis是0-1）。这两次剪裁功能相似，第一次的目的是减轻gpu负担。  

模板测试（stencil test）：可以理解为深度测试中的深度这个概念有开发者人为设定。  

blend（混合）/output merger

early-z

## 数学相关

点坐标：$$\left[ \begin{matrix}
        x \\
        y \\
        z \\
        1 \end{matrix} \right]$$ （如果是行向量，下边变换矩阵要转置）
方向矢量：$$\left[ \begin{matrix}
        x \\
        y \\
        z \\
        0 \end{matrix} \right]$$
基础变换矩阵：$$
\left[  \begin{matrix}
        M_{3*3} & t_{3*1} \\
        0_{1*3} & 1 
        \end{matrix}
\right]$$
之所以这样设置是为了使变换矩阵的计算结果正确；顶点变换中如果存在平移需要四维矩阵，方向矢量变换使用三维即可  

M：旋转缩放；t：平移（如果坐标点或向量是行向量，t的位置要换到左下角）  

复合变换依赖顺序，本质原因是矩阵乘法不满足交换律：$P_{new} = M_{translation} M_{rotation} M_{scale} P_{old}$ 执行顺序为从右到左，绝大多数情况按照缩放，旋转，平移的顺序  

空间变换流程：模型空间->世界空间->观察（相机）空间->剪裁空间（视锥体剔除）->屏幕空间（剪裁空间转NDC转屏幕像素）  

一般来说，模型空间到剪裁空间会合并为MVP矩阵（Model-View-Projection） 

## 光照模型

* BRDF（bidirectional reflection distribution function）
* BRDF经验模型（能量不守恒，简化的数学公式）：
  * Lambert：反射强度不受角度影响，反射角度受平面影响
  * 标准光照模型（Phong）：自发光，高光反射，漫反射，环境光（需要入射光，反射光，表面法线，视角方向）
  * blinn-phong：与phong相比不需要计算反射方向，取而代之的是视角和入射光线的平均值归一化后的结果
* 基于物理的BRDF模型（判断条件：是否满足交换律，即光路可逆；是否能量守恒）：
  * cook-torrance BRDF：微面元模型用来表示pbs（physical based shading）中的高光，D是法线分布函数，G是阴影遮蔽函数，F是菲涅尔反射函数
  * ward BRDF

实现细节：
* 漫反射符合兰伯特定律，即反射光线强度与表面法线和光源方向之间夹角的余弦值成正比  

## 纹理映射

纹理放大缩小的问题需要调整Filter Mode（Point,Bilinear,Trilinear）；
缩小时最常使用mipmapping（多级渐远纹理技术）：典型的用空间换时间（多33%的空间）  

bump mapping（凹凸映射）：分为两种，高度纹理（height map）模拟表面位移（displacement），得到一个修改后的法线值，称之为高度映射；另一种是法线纹理（normal map），直接做法线映射  

1.在切线空间下进行光照计算；2.在世界空间下计算，前者效率往往优于后者  

albedo是tex2D（CG的函数，对纹理进行采样）的结果；  
ambient是环境光  
diffuse是漫反射  
specular是高光  

法线纹理（normal map）可以使用DXT5nm的压缩格式，因为相比较普通图，法线纹理只有两个通道必不可少，第三个通道可以通过前两个推导出来，这种压缩方法可以减少内存占用  

## 透明效果

Alpha Test/Alpha Blending：透明度测试只有完全透明和完全不透两种可能；透明度混合可以实现半透明    

半透物体是开启深度测试但是关闭深度写入的，这导致渲染顺序变得十分重要（因为关闭了深度写入）；应该**渲染不透明物体之后再渲染半透明物体**；如果都是半透明，按相机距离排序，从后往前渲染，开启深度测试，但是关闭深度写入  

双面渲染：unity的Cull指令默认是Back，也就是背对相机的渲染图元不会被渲染  

## 渲染路径

更复杂的光照：
* 前向渲染：颜色缓冲区和深度缓冲区；unity的前向渲染有三种，逐像素处理（最强平行光和重要光源用这种方式），逐顶点处理，球谐函数（spherical harmonics）  
前向渲染的问题是，场景内有大量光源的情况下性能急剧下降，因为每个光源都要计算一次光照结果（一个光源一个pass）
* 延迟渲染：G-buffer（Geometry），包含两个pass，第一个使用深度缓冲计算哪些片元可见；第二个计算片元信息，即光照计算  
不支持抗锯齿；不能处理半透明；对硬件有要求MRT（multiple render targets）  
Unity的延迟渲染需要提供两个pass：第一个用于渲染G-buffer；第二个用于计算真正的光照模型

## API

Unity shader中的矩阵是按行优先的，Unity脚本中有个Matrix4x4是按列优先  

UnityRoot/Data/CGIncludes/ 里边有官方提供的.cginc文件，其中例如UnityCG.cginc十分值得学习  

# 《Direct12 3D游戏开发实战》——龙书

## 数学相关

view transform矩阵，观察空间到世界空间的坐标变化矩阵为：
$$
W = 
\left[  \begin{matrix}
        u_{x} & u_{y} & u_{z} & 0 \\
        v_{x} & v_{y} & v_{z} & 0 \\
        w_{x} & w_{y} & w_{z} & 0 \\
        Q_{x} & Q_{y} & Q_{z} & 1
        \end{matrix}
\right]
$$
其中，$$Q_{w} = (Q_{x},Q_{y},Q_{z},1)$$，$$u_{w} = (u_{x},u_{y},u_{z},0)$$，$$v_{w}$$还有$$w_{w}$$分别表示了观察空间中原点，x轴，y轴，z轴相对于世界空间的齐次坐标。  
相对的，世界空间到观察空间的变化矩阵为$$W^{-1}$$，世界矩阵可以分解为一个旋转矩阵和一个平移矩阵的乘积，即$$W=RT$$。
$$
V=W^{-1}=(RT)^{-1}=T^{-1}R^{-1}=T^{-1}R^{T}=
$$
$$
\left[  \begin{matrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & 0 & 1 & 0 \\
        -Q_{x} & -Q_{y} & -Q_{z} & 1
        \end{matrix}
\right]
\left[  \begin{matrix}
        u_{x} & u_{y} & u_{z} & 0 \\
        v_{x} & v_{y} & v_{z} & 0 \\
        w_{x} & w_{y} & w_{z} & 0 \\
        0 & 0 & 0 & 1
        \end{matrix}
\right]
=
\left[  \begin{matrix}
        u_{x} & u_{y} & u_{z} & 0 \\
        v_{x} & v_{y} & v_{z} & 0 \\
        w_{x} & w_{y} & w_{z} & 0 \\
        -Q_{x} \cdot u & -Q_{y} \cdot v & -Q_{z} \cdot w & 1
        \end{matrix}
\right]
$$
由此得到，
$$
V=
\left[  \begin{matrix}
        u_{x} & u_{y} & u_{z} & 0 \\
        v_{x} & v_{y} & v_{z} & 0 \\
        w_{x} & w_{y} & w_{z} & 0 \\
        -Q_{x} \cdot u & -Q_{y} \cdot v & -Q_{z} \cdot w & 1
        \end{matrix}
\right]
$$

# Unreal source code review

