---
title: 杂记：工具以及日常命令合集
date: 2020-11-16 11:59:11
tags:
---

# 网络相关

## windows

### 命令行设置代理

设置代理
netsh winhttp set proxy 127.0.0.1:10808
取消代理
netsh winhttp reset proxy
查看代理
netsh winhttp show proxy

### pip下载速度慢

python -m pip install --upgrade pip太慢

输入：
python -m pip install --upgrade pip  -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

其他下载链接：
豆瓣(douban) http://pypi.douban.com/simple/
阿里云 http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
anaconda 环境中pip install 第三方库下载较慢；

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas

### windows上使用linux

wsl和vm

# Adreno Profiler提取 网易镇魔曲手游美术资源