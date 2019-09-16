---
title: CYOU学习笔记
date: 2019-07-08 22:26:11
tags:
    - 工作笔记
    - 游戏开发
---

# Note

## 一. Unity

### cache server

If you switch Unity from iOS to Standalone mode for example, the imported texture will get a different hash. When switching the platform Unity calculates the new hash of all textures and tries to download them from the cache server. If they are available they will be used, otherwise it will import the texture and upload the imported result to the cache server.  
先算hash值，跟cache server上的比较，不一样就import，一样就download。节省时间

### streamingAssets 流式加载资源

todo

### 多个场景叠加，大场景处理

todo

### profiler

todo

### API

ScriptableObject的优点：
* 把数据真正存储在了资源文件中，可以像其他资源那样管理它，例如退出运行也一样会保持修改
* 可以在项目之间很好的复用，不用再制作Prefab那样导入导出

看了下感觉有很多东西都可以用它。之前的做法一般都是[Serializable]一个class，然后在面板里配数据，做成prefab，但这种方法没有上面的优点。感觉今后如果有类似通过Serializable + Class + Prefab实现存储数据的想法的时候，都应该先考虑下能不能用ScriptableObject做成一个真正的资源文件。

### Unity的各种意外

杀毒软件的锅，卸载就好  

场景贴图丢失（紫色），原因是svn导致的meta文件不一致，revert掉meta文件，让unity自动从cache server更新一遍就好

## 二. 语法/规范

### lua

使用闭包，可以避免动态编译。
**闭包/闭包组成**：外部函数+外部函数创建的upvalue+内部函数（闭包函数）  
``` lua
    function test()
        local i=0
        return function()//尾调用
            i+=1
            return i
        end
    end
    c1=test()
    c2=test()//c1,c2是建立在同一个函数，同一个局部变量的不同实例上面的两个不同的闭包
            //闭包中的upvalue各自独立，调用一次test（）就会产生一个新的闭包
    print(c1()) -->1
    print(c1()) -->2//重复调用时每一个调用都会记住上一次调用后的值，就是说i=1了已经
    print(c2())    -->1//闭包不同所以upvalue不同    
    print(c2()) -->2
```

访问外层局部变量（也就是外一层函数的局部变量）并没有访问局部变量快，但是仍然比访问全局变量快。  
除非需要真正动态地执行代码，比如代码是由用户输入的，其他情况则很少需要编译动态的代码。  

'#'不是获取table长度,是获得一个table中最大的数字键值    

lua中的面向对象:    

metatable:Lua 查找一个表元素时的规则，其实就是如下3个步骤:
  1. 在表中查找，如果找到，返回该元素，找不到则继续
  2. 判断该表是否有元表，如果没有元表，返回 nil，有元表则继续。
  3. 判断元表有没有 __index 方法，如果 __index 方法为 nil，则返回 nil；如果 __index 方法是一个表，则重复 1、2、3；如果 __index 方法是一个函数，则返回该函数的返回值。

__newindex:当你给表的一个缺少的索引赋值，解释器就会查找__newindex 元方法：如果存在则调用这个函数而不进行赋值操作。   

判断table是否为空的方法
``` bash
a={}
if next(a) ~=nil then dosomething end
```   

**:和.的区别** ":"可以理解为作用域

数组第0项是nil 从1开始

### C++

do{ } while(false)的作用：
* 是经典的安全资源释放方法？
* return early 的一种写法, 多个 return 会使代码变得混乱, 通过 do while 进行流程控制可以 做到一个入口 一个出口. 而且可以避免 if else 嵌套 阻止箭头形代码的形成

/#pragma
* /#pragma 用于指示编译器完成一些特定的动作；
* 它所定义的很多指示字是编译器特有的；
* /#pragma message 用于 自定义编译消息、#pragma once 用于保证头文件只被编译一次、**#pragma pack 用于指示内存对齐方式**。  

宏定义#define 一个应用场景是跨平台，根据不同平台给统一的接口分配不同的方法  

int类型的与或运算 是二进制形式下的运算

### C#

位运算符：& | ^ ~ >> <<  
应用：
``` C#
int average(int x, int y) //返回X,Y的平均值 
{ 
return (x&y)+((x^y)>>1); 
} 
```

map hashmap pair

uint和int区别在于正负，int64和int32区别在于范围

## 三. PZ

### 客户端资源管理

assetbundle，axpfilesystem

### 导航系统

1. PA客户端（也就是我们的客户端）用了UNITY的一个叫A* pathfinding project的一个2013年插件
2. 天龙服务器（我们的服务器），基于点阵的一个A* 2D导航算法
3. Unity本身自带的Navigation，Unity把做Recast的那个人收编，基于Recast进行深度修改的一个导航系统
4. Recast，一个开源的导航系统

### CYDynamicSky

todo

## 四. 功能

panel prefab必须放panel文件夹下  
逻辑脚本必须放同名文件夹下，文件夹、脚本命名都得和预制体一样  
第一次点击头像不会clone出practicepanel，显示有**正在加载500，第二次可以，关闭之后就没有其他ui了  

保释面板注册什么事件？
事件是在luaevent里新加的 OpenPirateBailPanel  
luaevent里字符串的前缀大写字母含义？  
注意 "."和":" 的区别  
UIModule下 modulename是创建panel _G.Pirate_BailPanel = BaseUI:new("Pirate_BailPanel") 的脚本的名字 不是pirate module   

问题：onevent的p_param怎么确定第几个是什么含义的，在哪儿约定的  

[Lua]ProtectedCall Error:UI/Pirate_BailPanel/Pirate_BailPanel:37: attempt to index a nil value
attempt to index local 'script' (a nil value)
**原因/解决方法**：open之后panel不是同步打开的，也就是说open之后的逻辑执行时还没有panel，所以getUIModule是nil  
调用start时，panel加载完了，所以把getUIModule放start里了

看bagmodule 了解如何获取icon：self:SetTextureRes(uiModule.List_Texture:get_Item(0), BagModule:GetItemIconById(costItemID))

打开tip用哪个TipsModule.EnumTipsOpenType  
EventSender.SendEvent(LuaEvent.ShowPublicTip, lang(23010));  

时间：需要xx小时xx分xx秒的，还有浮点数的，两种（抛给外边做了）  
public tip怎么显示两种以上的材料（策划决定，改成点击图标显示tip了）  

self:InitItemPanel(ctrl, go) 需要gameobject符合UIModule的命名规范 之后就可以随意改了

需要物品太多/或者没有 怎么处理？  

**修改**：
接口就一个time，内部转换时间，算所需物品数量，回调都不用了  
弹出框读表得改，icontexture、qualitysprite、背包内物品剩余数量 有新街口  


## 五. BUG

21196	【主干】【bug】【主线任务】潜入亚得里亚海id:1000107任务文字覆盖   
baseTaskAndTeamUI(Clone)  1000107 已解决  
21235	【主干】【bug】【主线任务】潜入亚得里亚海id：1000107  任务副本的大小和特效表现的不匹配	游戏bug 	
美术素材原因,已经让策划去向美术提需求(篮圈大小)  
20881	【主干】【BUG】【船只航海士系统】航行事件升级，提示的是给玩家增加经验	游戏bug	打开, assigned  
客户端C#和lua搜不到strid 110129,在服务器代码上
17521	【主干】【BUG】【航行事件】航行事件图标消失问题	游戏bug	打开  
sailingevent 预制 功能取消不用看了


## 六. 热更

SLua、Tolua、XLua和ILRuntime  
babelua生成lua脚本

## 七. 服务器

[游戏服务器开发所需知识点总结](https://cloud.tencent.com/developer/article/1349061)  
[TCP socket心跳包实例程序](https://cloud.tencent.com/developer/article/1342680)  

消息协议,共享内存和数据库   
一般来说除去所有的显示相关的部分，比如技能特效，施法动作，伤害冒字，UI等等，剩下的做到服务器就可以了  

select 实现多路IO复用  

消息驱动 再看看

## 八. 压测（Locust）

run_master-->run_slave-->GameLocust()-->action-->消息包  
I_sailing_battle.py-->ACFSailingForRobot.py-->PACKETS-->Defines  
actions中的__init__.py中需要添加ACGNavigatorOperation  

init_context 什么时候需要？航海士测试中不需要  

### 航海士流程：

* 玩家角色升到50级
* 造艘船
* 拥有所有航海士
* 高中低经验书
* 一键任命/两种航海士升级方式/使用一个航海士经验道具/主舰航海士一键升级/万能碎片兑换/航海士碎片合成/航海士升星

积分商店流程：  
* GM30000银币（交子）-->买一个木材
* 请求商店列表（ParentId，SubId）

python 255用byte接收是-1？ chr(255)  

不要在handle里（接受GC消息）直接跟action做交互，self会乱，无限递归？  

Functions.py里为什么是
``` bash
if packet.__class__.__name__ == packetname:
```
packet.__class__.__name__是str而不

covenantpropert 契约人信息  
TroveSkillMain 发现物技能  

trovemain里有寻路坐标场景id

### 发现物流程：

* 激活（解锁）    满足前置条件
* 线索           PACKET_CG_CLUE_COMPLETE    1
* 技能等级        没法主动升
* 签约           
* 发现发现物？    PACKET_CG_TROVE_FIND
* 待完成契约      
* 发现物上报      PACKET_CG_TROVE_REPORT

CGAskTroveData      --      PACKET_CG_TROVE_DATA      =   2453     请求发现物数据
CGTroveComplete     --      PACKET_CG_TROVE_COMPLETE  =   2482     请求发现物数据（包含撕毁契约）
CGClueComplete      --      PACKET_CG_CLUE_COMPLETE   =   2488     请求线索完成
CGTroveFind         --      PACKET_CG_TROVE_FIND      =   2512     请求发现物发现条件是否满足
CGAdvPointModify    --      PACKET_CG_ADVPOINT_MODIFY =   2527     请求发现物冒险点数更改
CGTroveReport       --      PACKET_CG_TROVE_REPORT    =   2700     请求发现物上报

GCAskTroveData      -- PACKET_GC_TROVE_DATA = 2454         返回请求发现物数据
GCAdvPointModify    -- PACKET_GC_ADVPOINT_MODIFY = 2528    返回请求发现物冒险点数更改
GCAdvSkillLevelUp   -- PACKET_GC_ADVSKILL_LEVELUP = 2485   返回请求冒险技能升级
GCClueComplete      -- PACKET_GC_CLUE_COMPLETE = 2489      返回请求线索完成
GCTroveComplete     -- PACKET_GC_TROVE_COMPLETE = 2483     返回请求发现物数据
GCTroveFind         -- PACKET_GC_TROVE_FIND = 2513         返回请求发现物发现条件是否满足
GCTroveLevelUp      -- PACKET_GC_TROVE_LEVELUP = 2487      返回请求冒险等级提升
GCTroveReport       -- PACKET_GC_TROVE_REPORT = 2701       同步发现物上报

问题 发现物状态m_TroveState在那个表
已解锁和可发现什么区别  
主动升级技能 签约

socket errno10053 别用waitforpacket_with_heartbeat 用waitforpacket  
同一场景下（场景号相同）只输xz坐标是瞬移

发现物上报需要npcid troveid还有trovestate符合要求  
Error! packet.filldatafromstream error  
**原因是python的list不能直接用索引赋值，只能用append加值，或者理解为给第i项初始化**

GM指令在游戏里能用 压测脚本用不了
sharememory说trovedata保存失败
UI\Trove\DiscoveryListUI.lua 194行有nil 估计时表错了 但是没更新突然出这错
莫名其妙换了新号就好了 清库也没法测旧号了
执行到后半段必定10053掉线，不知道为什么
**因为前一个action消息包发错参数了**
goto 传不到港口了

### 无尽航程流程

action：
ACGAskHeroTrialsChallenge   请求进入挑战
AGCReHeroTrialsInfo         玩家挑战信息
ACGAskGetFirstAward         首通奖励
AGCFirstAwardListInfo       可领首通奖励列表
ACGAskHeroTrialsSeckill     扫荡

前期准备：  
  升级99  
  造船两艘 指定副舰  
  切职业 提升攻击力  
  补给、船员、疲劳度 
流程：
  状态机：战斗状态和准备进入下一关状态间的转换条件
    发请求进入挑战包 进入战斗状态  
    计时

waitforpacket/withheartbeat//socket.error: [Errno 10053] 
这能都改成waitforpacket吗？？？  
不用改成waitforpacket，问题出在
``` bash
self.person['nNextLevelId_current'] = self.person['nNextLevelId'] # 写反成
self.person['nNextLevelId'] = self.person['nNextLevelId_current'] # 了
```
AGCFirstAwardListInfo 总是false  
登陆时就会发一次

### 世界boss流程

系统时间需要在指定时间 开始时间是12:40跟21:40，5分钟后刷新BOSS，35分钟后活动结束  
测试可以改系统时间触发活动  

造船 带附舰
35/45/55级
选择职业
根据等级传到指定场景坐标
打

pip install pypiwin32（不改系统时间了改表）  
改公共表只需重启服务器，服务器复制的是客户端转表前的表

世界boss的倒计时要看服务器时间，什么时候同步时间？  
handle 在functions里加handlelist  

### 好友流程

一个client 五个otherperson  
登陆-->搜索-->加好友-->查在线状态-->关注/取消关注-->拉黑/取消拉黑
-->创建三个分组（最多三个）-->加人-->删分组-->删好友

sendpacket出错是前一个发的包多传了参数

ACGChat_Friend直接用起来有点问题

### 商会流程

GC包怎么传参数进去？PACKET_GC_GUILD要一个self['m_PacketType']  
0822 做禅让和通过的消息包

## 九. TA相关

houdini制作HDA/开发HDA  
反射探针（Reflection Probe） 合批 batch  


## 十. BITool

数据库相关  
excel-->sql/json-->建表/拷贝json到pattern文件夹-->C#代码添加json-->log文件放入path-->.net工具导入表  
要给什么赋默认值 多半是json出错 数据没进去 所以需要默认值  
fleettask有个数组越界 像是日志项数和json不匹配：json54项算上时间，日志里只有53  
语法错误要看具体sql语句，fleettask这个最后是,) 就是excel里多了（红色的是没进服务器的） 服务器（实际的log日志里没有） 解决方法是先删掉excel的行  
登陆点的log有错 开一去查了 先跳过这个  
excel里有cylog里没有的是测试没跑这功能，汇总给开一  
替换旧的json/sql都得替换  

不能为null的是因为策划表里能不能为空那项不对，手动改sql not null那项  
C#脚本bug：log不能正好是十行  

ERROR 2003 (HY000): Can't connect to MySQL server on 'localhost' (10061)  百度有解决方法

## 优化

合批优化，GPUInstance优化  
性能分析工具？帧数据  
合批？  

## billing

# TODO

框架层 线程模型 网络通信模型 跳转 线程安全