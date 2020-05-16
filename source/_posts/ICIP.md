---
title: SEE THROUGH OCCLUSIONS:DETAILED HUMAN SHAPE ESTIMATION FROM A SINGLE IMAGE WITH OCCLUSIONS
date: 2020-03-31 12:45:53
tags:
    - ICIP
    - 三维人体重建
    - 深度学习
    - shift_net
    - hmd
---

# SEE THROUGH OCCLUSIONS:DETAILED HUMAN SHAPE ESTIMATION FROM A SINGLE IMAGE WITH OCCLUSIONS

## Abstract

3D human body shape and pose reconstructing from a single RGB image is a challenging task in the field of computer vision and computer graphics. Since occlusions are prevalent in real application scenarios, it’s important to develop 3D human body reconstruction algorithms with occlusions. However, existing methods didn’t take this problem into account. In this paper, we present a novel depth estimation Neural Network, named Detailed Human Depth Network(DHDNet), which aims to reconstruct the detailed and completed depth map from a single RGB image contains occlusions of human body. Inspired by the previous works [1, 2], we propose an end-to-end method to obtain the fine detailed 3D human mesh. The proposed method follows a coarse-to-fine refinement scheme. Using the depth information generated from DHDNet, the coarse 3D mesh can recover detailed spatial structure, even the part behind occlusions. We also construct DepthHuman, a 2D in-the-wild human dataset containing over 18000 synthetic human depth maps and corresponding RGB images. Extensive experimental results demonstrate that our approach has significant improvement in 3D mesh reconstruction accuracy on the occluded parts.

## Status

ICIP under review -- 2020.1.31  
ACCEPTED          -- 2020.5.16  

{% asset_img accepted.png review %}  

## Links

{% pdf ICIP.pdf %}

{% asset_img 6.PNG details %}  
{% asset_img 7.PNG depth %}  
{% asset_img Capture.PNG comparison %}  
{% asset_img system6.png end-to-end system %}  