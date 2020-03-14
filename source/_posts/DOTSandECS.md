---
title: DOTS & ECS & RP
date: 2020-03-04 18:19:17
tags:
    - Unity
    - ECS
    - DOTS
---

## About ECS
OLD:  
    GameObjects & MonoBehaviours  
    Object-oriented  
    create一个叫Player的GameObject，用若干MonoBehaviour作为Player的组件，实现功能（例如renderer,physics,movement）。

NEW:  
    Entities & Components & Systems  
    data-oriented  
1. group together components
2. contain data (只是数据结构，不包含逻辑)
3. contain behaviour （逻辑只在这里）

就是数据和逻辑分开了，这样cpu可以读到连续的内存，不需要每个GO来回在内存里跳

### Note
``` C#
World.Active.EntityManager; // desperated
World.DefaultGameObjectInjectionWorld.EntityManager; // use this

typeof(RenderBounds); // make the mesh visable
```

## DOTS
DATA ORIENTED TECHNOLOGY STACK  
三部分组成：
1. C# Job system
   1. 多线程，unity的性能问题主要来源于主循环update线程是单线程的
   2. C#创建线程并管理每个线程的工作很困难，job system来管理线程，并且分配任务（assigns jobs）
2. entity component system
3. burst compiler
   1. 把C#编译成高度适用于Job system的机器码


## Render Pipeline
Scriptable render pipeline SRP  
Universal render pipeline URP(LWRP)  
High definition render pipeline(HDRP)  

Build-in renderer