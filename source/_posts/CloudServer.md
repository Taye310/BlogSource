---
title: 云服务器相关
date: 2020-02-12 20:00:24
tags: 
    - 云服务
    - 腾讯云
---

# 云上项目

## Hotfix

[xlua到webgl的坑](http://blog.okbase.net/unity3d/archive/56120.html)  

``` lua
xlua.hotfix
```

## ChatRoom

Mirror聊天室

Mysql更改user的host地址：
``` sql
update user set host = '%' where user = 'root';
```

改成linux之后要重新做server了  

## Home

http://providencezhang.cn  
vuejs+node+nginx [link](https://segmentfault.com/a/1190000018099632)  
[三者的关系](https://www.zhihu.com/question/294219455?sort=created)  
简单来说，nginx可以反向代理多个node项目，做负载均衡等。如果没有服务端逻辑无需node，vuejs+nginx即可  

## Blog

blog.providencezhang.cn 解析到了 taye310.github.io  
hexo + github pages只能提供静态页面，unity webgl需要网页服务器能解析.unityweb文件，在IIS上需要在mapping上单独设置（mimetype），这个可能是导致不能在github pages上部署unity webgl项目的原因。

## 计划

要不要直接换skynet - 需要Ubuntu环境 √
消息机制是不是可以自己实现一套，看skynet吧  

xlua热更demo实现  
C#这个attribute到底怎么用

## 日志

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

### 2020.2.19
刷leetcode，首页整好看点！！！找个模板，后端用wordpress集成什么意思？？  
域名备案终于下来咯

### 2020.3.9
ubuntu上不要用系统代理（更新conda包会报错未知sock版本），chrome用Omega插件，命令行用proxychain4  
Skynet  
腾讯云上想用skynet的话要用ubuntu  
这样的话主页要换成nginx，不想装图形界面了，用共享文件夹samba远程写脚本，到linux下build  

### 2020.3.10
云服务器重装了ubuntu，用vscode remote development就可以远程调试，ssh添加了两对，一是新建的Home，二是github用的在.ssh里的一对  
[samba配置教程](https://blog.csdn.net/qq_28719743/article/details/84872396)  
传文件用sftp就好，局域网可以用samba

### 2020.3.11
``` nginx -s reload ```  
[conf](https://blog.csdn.net/WanJiaBaoBao/article/details/83349622)  
Nginx location设置二级域名时 root下边要有这个名字的文件夹  
``` bash
server{
        listen 80;     #1.你想让你的这个项目跑在哪个端口
        server_name providencezhang.cn;     #2.当前服务器ip
       	location / {
        	root /home/ubuntu/ftp/www/home;     #3.dist文件的位置(我是直接放在home目录下了) 
            # try_files $uri $uri/ /index.html;     #4.重定向,内部文件的指向(照写)
        }
		location /static {
        	alias /home/ubuntu/github/simpleweb;     #3.dist文件的位置(我是直接放在home目录下了) 
            # try_files $uri $uri/ /index.html;     #4.重定向,内部文件的指向(照写)
        }
        location /api {  #4.当请求跨域时配置端口转发
            proxy_pass http://175.24.57.128:8848/api; #5.转发地址
        } 
    }
```

### 2020.3.12
用firewall-cmd开nginx的80端口

### 2020.3.13
最终目标：多人在线游戏，用dots  
1. skynet源码  
2. 简单demo跑通逻辑（登陆，心跳，消息机制）
3. 客户端开发
4. 前后端连接

### 2020.3.14
[git代理设置](https://echo.xuchaoji.com/index.php/archives/110/)

### 2020.3.26
dots到webgl 会出现问题 [link](https://forum.unity.com/threads/bug-crash-with-a-fresh-project-on-ios-monopinvokecallback.827634/)  
``` conf
sudo nginx -t         # 测试配置是否成功
sudo nginx -s reload  # 重启服务
```
xlua的热更到webgl有问题

### 2020.9.15
做games-cn的作业需要图形界面，用vnc+xfce  

连接不到server：原因是防火墙策略  
> 保存防火墙规则命令：iptables-save > /opt/iprules_all.txt
> 清除策略iptables -F
> 后续需要恢复原本的防火墙策略，通过如下命令恢复：iptables-restore < /opt/iprules_all.txt

vncviewer登录后显示叉：~/.vnc/xstartup配置文件有问题（权限或者内容），查看vnc log解决  

常用命令：  
> ps -ef|grep vnc
> vncserver -kill :1
> vncserver :1