---
title: C++&C# notebook
date: 2019-02-18 09:06:46
tags:
    - C++
    - C#
categories: 学习笔记
---

# C++

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


# C#

静态多态性：函数重载、运算符重载  
动态多态性：抽象类和虚函数（抽象类和接口的区别：抽象类比接口更详细点，可以继承多个接口，但只能一个类）

**正则表达式得看看todo**