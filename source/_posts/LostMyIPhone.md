---
title: 给曦哥买了个仓鼠叫叉叉——IPhoneX的叉
date: 2018-10-23 08:02:23
tags: 
    - 信息安全
    - XSS
    - 钓鱼网站
    - burpsuite
---

# 钓鱼网站攻击记录

## XSS
_cross site script_
网页里有input都可以插入html代码，一般是返回服务器的cookie，找到服务器管理员的相关信息。
也可以从url插入代码

## burpsuite
功能强大的web攻击集成环境，community版本提供大部分功能，但是需要手动设置参数，企业版提供scanner扫描漏洞。

## 已知的钓鱼网站防护
1. 限制input长度
2. 将input的值使用document.* 方法转为%..%..样式的字符串，使其无法在html中编译
3. 限制ip，每次进入网页的url都有唯一编码，看起来是md5加密的，一旦提交过信息封ip
