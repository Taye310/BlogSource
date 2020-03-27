---
title: C++ & C#/Unity notebook
date: 2019-02-18 09:06:46
tags:
    - C++
    - C#
    - Unity
    - notebook
categories: 学习笔记
---

# C/C++

vector & list: 
vector方便随机查询；扩容时因为它使用内存是连续的，会申请块更大的内存，造成整块内存的拷贝  
list由双向链表实现，好增删，不好查询  

[decltype](https://www.cnblogs.com/ghbjimmy/p/10636030.html):有时我们希望从表达式的类型推断出要定义的变量类型，但是不想用该表达式的值初始化变量（初始化可以用auto）。为了满足这一需求，C++11新标准引入了decltype类型说明符，它的作用是选择并返回操作数的数据类型，在此过程中，编译器分析表达式并得到它的类型，却不实际计算表达式的值。  

``` C++
int getSize();
​
int main(void)
{
    int tempA = 2;
    
    /*1.dclTempA为int.*/
    decltype(tempA) dclTempA;
    /*2.dclTempB为int，对于getSize根本没有定义，但是程序依旧正常，因为decltype只做分析，并不调用getSize().*/
    decltype(getSize()) dclTempB;
​
    return 0;
}
```

在C中，使用typedef定义struct在创建结构体是就不需要``` struct Student stu; ```了，直接使用typedef定义的别名例如S，``` S stu; ```

unordered_map不能使用pair作为键值，需要提供pair的hash函数，map可以  

hash_map与unordered_map: 前者使用一个下标范围比较大的数组来存储元素，形成很多的桶，利用hash函数对key进行映射到不同区域进行保存；
后者记录元素的hash值，根据hash值判断元素是否相同。  
速度上2最优其次hash_map最次map  

&  （位   “与”）  and  
^  （位   “异或”）  
|  （位   “或”）   or  
~  （位   “取反”）  

位移运算符(<</>>)：乘以/除以$2^n$

整型最大最小值：INT_MIN,INT_MAX

map<>如果不赋初值，不是NULL是0

[vector](http://www.cnblogs.com/Nonono-nw/p/3462183.html)：向量
``` bash
#include <vector>;
```
[iterator](https://www.cnblogs.com/maluning/p/8570717.html)：迭代器  

[STL中的基本容器](https://www.cnblogs.com/cxq0017/p/6555533.html)  
顺序容器：vector，list，deque等
关联容器：map，set等

upper_bound, lower_bound:  
``` bash
// lower_bound/upper_bound example
#include <iostream>     // std::cout
#include <algorithm>    // std::lower_bound, std::upper_bound, std::sort
#include <vector>       // std::vector

int main () {
  int myints[] = {10,20,30,30,20,10,10,20};
  std::vector<int> v(myints,myints+8);           // 10 20 30 30 20 10 10 20

  std::sort (v.begin(), v.end());                // 10 10 10 20 20 20 30 30

  std::vector<int>::iterator low,up;
  low=std::lower_bound (v.begin(), v.end(), 20); //          ^
  up= std::upper_bound (v.begin(), v.end(), 20); //                   ^

  std::cout << "lower_bound at position " << (low- v.begin()) << '\n';
  std::cout << "upper_bound at position " << (up - v.begin()) << '\n';

  return 0;
}
```

a++/++a
``` bash
int a = 1;
cout<<a++<<endl;  // 1
cout<<a<<endl;    // 2
```

``` bash
vector<int> &nums;
for(auto i : nums){}
```

unsigned 无符号的  

[unordered_map](http://www.cplusplus.com/reference/unordered_map/unordered_map/?kw=unordered_map)

C++ struct 构造函数附默认值的写法：
``` bash
struct student{
    int age;
    student *child;
    bool sex;
    int check;
    student(int input):age(input),child(nullptr),sex(true),check(1996){}
};

int main(){
    student a = student(18);
    cout<<a.age<<a.sex<<a.check<<endl;
    return 0;
}
```
out
``` bash
1811996
```

把指针运算符 * 应用到 var 上是完全可以的，但修改 var 的值是非法的。这是因为 var 是一个指向数组开头的常量，不能作为左值。[C++](https://www.runoob.com/cplusplus/cpp-pointers-vs-arrays.html)  

**指针**int var; //var 输出：20  
int* p; p = &var; //p 输出：地址   
////////////////////*p 输出：20  
**引用**int& a; a = var; //a 输出：20  

所有指针的值的实际数据类型，不管是整型、浮点型、字符型，还是其他的数据类型，都是一样的，都是一个代表内存地址的长的十六进制数  

引用很容易与指针混淆，它们之间有三个主要的不同：  
  1. 不存在空引用。引用必须连接到一块合法的内存。  
  2. 一旦引用被初始化为一个对象，就不能被指向到另一个对象。指针可以在任何时候指向到另一个对象。  
  3. 引用必须在创建时被初始化。指针可以在任何时间被初始化。 

试想变量名称是变量附属在内存位置中的标签，您可以把引用当成是变量附属在内存位置中的第二个标签。因此，您可以通过原始变量名称或引用来访问变量的内容。  

new动态分配内存（只能new一个指针吗？不是），delete删除，delete [] pvalue

[变长数组](https://blog.csdn.net/fanyun_01/article/details/77430682) 普通数组到vector 一维到多维  

模板：函数模板/类模板  

内联函数（inline属于ret-type）：啥时候用，ret-type还包括哪些？  

**boost库**：准标准库

`string::find("a")` 如果没有找到"a"，会返回一个固定的大数，且等于`string::npos` 的值

# C#

struct是值类型，内存分配在栈上；  

Action与Func是特殊的delegate，用event修饰的delegate更加安全。  
EventHandler就是一个已经声明出来的delegate  

**where and new()**
在C#中，泛型的使用非常广泛，为了泛型调用安全，经常需要对所使用的类型进行约束。  
在对泛型的约束中，最常使用的关键字有where 和 new。  
其中where关键字是约束所使用的泛型，该泛型必须是where后面的类，或者继承自该类。  
new()说明所使用的泛型，必须具有无参构造函数，这是为了能够正确的初始化对象  

静态多态性：函数重载、运算符重载  
动态多态性：抽象类和虚函数（抽象类和接口的区别：抽象类比接口更详细点，可以继承多个接口，但只能一个类）

**正则表达式得看看todo**

装饰器 attribute 方法前边直接加个函数的区别


# Unity

矩阵对应的几何变换 https://orangered3stones.iteye.com/blog/1940821  
对于N+1维坐标表示的理解 https://www.cnblogs.com/btgyoyo/p/7085264.html  
碰撞检测 http://www.jmecn.net/tutorial-for-beginners/chapter-15-collision-detection.html

基于组件的引擎架构：  
派生关系，通过继承父类获得父类的功能，这些通用功能为了能够为各种派生类提供服务，都必须实现到基类中  
不再是父类中的接口，而变成子对象实例，为游戏对象提供服务  
组合和继承的区别  
gameobject都派生自object 为什么  
coroutine 生命周期 c#的语法 反射 代理 设计模式 工厂 单例 装饰器  
设计模式 shader

# todo

C++ 语法，算法，引擎：A*再来一遍，多线程，模板，迭代器，网络同步  
Unity 网络Unet，Mirror