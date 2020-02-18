---
title: 云服务器相关
date: 2020-02-12 20:00:24
tags: 
    - 云服务
    - 腾讯云
---

# 云上项目

## UnityWeb

Mirror聊天室

**日志：**
### 2020.2.10
服务器win版本，客户端webgl，IIS部署成功

### 2020.2.12
业务：增加聊天记录；实现：不论是用streamasset还是加mysql数据库，服务器和客户端内容都需要分开  
server记聊天记录 client是不用记的  
command不能有返回值，传入参数类型也有限制，正确的方法：
```
but yeah you cant do that, I use ClientRpc's so for example if i have a float that's called "exampleValue" and want to update it on the client you could something like this:

[Command]
public void CmdRecuestNewValues(){
RpcGiveNewValues(exampleValue);
}

[ClientRpc]
public void RpcGiveNewValues(float value){
exampleValue = value;
}

then if you call the CmdRecuestNewValues(); command you will update you values.
```

### 2020.2.14
unity URP vs HDRP

**计划：**
要不要直接换skynet - 需要Ubuntu环境

## IIS_Index

首页，vuejs/vant组件。怎么整怎么丑，还没想好加什么业务。

## Blog

blog.providencezhang.cn解析到了taye310.github.io  
hexo + github pages只能提供静态页面，unity webgl需要网页服务器能解析.unityweb文件，在IIS上需要在mapping上单独设置，这个可能是导致不能在github pages上部署unity webgl项目的原因。