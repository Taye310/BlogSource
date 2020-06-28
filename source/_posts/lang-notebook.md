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

[右值引用与move()\forward()函数](https://blog.csdn.net/coolmeme/article/details/44459999)：std::move执行一个无条件的转化到右值，更像是"rvalue_cast<T>"；std::forward把其参数转换为右值，仅仅在那个参数被绑定到一个右值时；右值引用的目的是减少数据拷贝，提升性能  

[虚继承](http://c.biancheng.net/view/2280.html)：解决菱形继承问题  

在C++中，内存分成5个区，他们分别是堆、栈、自由存储区、全局/静态存储区和常量存储区  
1. 栈，就是那些由编译器在需要的时候分配，在不需要的时候自动清楚的变量的存储区。里面的变量通常是局部变量、函数参数等。
2. 堆，就是那些由new分配的内存块，他们的释放编译器不去管，由我们的应用程序去控制，一般一个new就要对应一个delete.如果程序员没有释放掉，那么在程序结束后，操作系统会自动回收。
3. 自由存储区，就是那些由malloc等分配的内存块，他和堆是十分相似的，不过它是用free来结束自己的生命的。
4. 全局/静态存储区，全局变量和静态变量被分配到同一块内存中，在以前的C语言中，全局变量又分为初始化的和未初始化的，在C++里面没有这个区分了，他们共同占用同一块内存区。
5. 常量存储区，这是一块比较特殊的存储区，他们里面存放的是常量，不允许修改(当然，你要通过非正当手段也可以修改)
？？

[头文件声明static变量，多个文件include该头文件](https://bbs.csdn.net/topics/390720572)，会导致每个文件都有一个专属的static变量  

const的物理常量性和逻辑常量性：物理常量性就是const对象不能改变，但是可以```*a.ptr=anything;```，逻辑常量性用```mutable```关键字保证，mutable的成员变量在const成员函数中也是可以改变的  

constexpr：constexpr所修饰的变量一定是编译期可求值的，runtime的时候不能赋值，不然会报错，所修饰的函数在其所有参数都是constexpr时，一定会返回constexpr。  

泛型技术：说白了就是试图使用不变的代码来实现可变的算法。比如：模板技术，RTTI技术，虚函数技术，要么是试图做到在编译时决议，要么试图做到运行时决议。  

重载set的 oprater < 就可以使set内部按特殊要求有序 LFUCache

全局对象的构造函数会[在 main 函数之前先运行](https://www.cnblogs.com/zpcoding/p/10805639.html)

[extern与static](https://www.cnblogs.com/wh5313/archive/2012/06/12/2546112.html)：没有链接属性的标识符（none）总是被当做单独的个体，也就是说该标识符的多个声明被当做独立不同的实体。属于internal链接属性的标识符在同一个源文件内的所有声明中都指同一个实体，但位于不同源文件的多个声明则分属不同的实体。属于external链接属性的标识符不论声明多少次、位于几个源文件都表示同一个实体。  

[定义与声明](https://www.cnblogs.com/damaohai/p/11497143.html)：区别在于是否分配空间（extern）  

do...while(0)的作用：宏定义函数的时候解决“；”所带来的问题。宏跟函数的区别在于宏是把参数替换到指定位置（++a的例子），imgui中也有提到  

C++类的内部可以定义引用数据成员，必须通过成员函数初始化列表初始化  

const修饰的属性只能在构造函数里初始化，然后就不能用变量名改值了，但是可以直接控制变量所在的地址直接修改值  

#pragma once：避免include重复引用一个文件  

空类的sizeof为1：那是被编译器插进去的一个char ，使得这个知class的不同实体（object）在内存中配道置独一无二的回地址。

类型安全很大程度上可以等价于内存安全，类型安全的代码不会试图访问自己没被授权的内存区域  

``` delete p; ``` 实际意思是删除了p所指的目标（变量或对象），释放了它所占的堆空间，而不是删除p本身（指针p本身并没有撤销，它自己仍然存在，该指针所占内存空间并未释放，指针p的真正释放是随着函数调用的结束而消失），释放堆空间后，p成了"空指针"。如果我们在delete p后没有进行指针p的制空（p=NULL)的话，其实指针p这时会成为野指针，为了使用的安全，我们一般在delete p之后还会加上p=NULL这一语句  

包含纯虚函数的基类可定义指向派生类对象的基类指针和派生类对象的引用，不能直接定义自身对象  

[print输出格式控制](https://blog.csdn.net/qq_37059136/article/details/80841675)

vecotr的at和[]: v是个空集合的情况下，[]访问是行为未定义的，at访问则会抛出std::out_of_range异常。c++标准不要求vector<T>::operator[]进行下标越界检查，原因是为了效率，总是强制下标越界检查会增加程序的性能开销。设计vector是用来代替内置数组的，所以效率问题也应该考虑。  

unique_ptr是智能指针的一种  

comptr和unique_ptr的区别：  

``` C++
auto_ptr<string> aps(new string("abd"));
	auto_ptr<string> aps2;
	aps2 = aps;
	cout << *aps << endl;//报错 此时aps已经失去对string内存的所有权，如果是两个普通指针，则没有问题
	cout << *aps2 << endl;
```

implicit conversion/explicit conversion:

#pragma comment ( lib,"wpcap.lib" )  
表示链接wpcap.lib这个库。和在工程设置里写上链入wpcap.lib的效果一样（两种方式等价，或说一个隐式一个显式调用），不过这种方法写的 程序别人在使用你的代码的时候就不用再设置工程settings了。告诉连接器连接的时候要找ws2_32.lib，这样你就不用在linker的lib设置里指定这个lib了。  

C++的钻石继承：dreaded diamond：  

函数声明后边的const：const的函数不能对其数据成员进行修改操作。const的对象，不能引用非const的成员函数。  

noexcept：该关键字告诉编译器，函数中不会发生异常,这有利于编译器对程序做更多的优化。  
如果在运行时，noexecpt函数向外抛出了异常（如果函数内部捕捉了异常并完成处理，这种情况不算抛出异常），程序会直接终止，调用std::terminate()函数，该函数内部会调用std::abort()终止程序。  

[class和struct的区别](https://zhidao.baidu.com/question/748004411503788052.html)：最根本的引用类型和值类型

volatile: A volatile specifier is a hint to a compiler that an object may change its value in ways not specified by the language so that aggressive optimizations must be avoided.

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
减少了函数调用，但是增加目标代码的大小

**boost库**：准标准库

`string::find("a")` 如果没有找到"a"，会返回一个固定的大数，且等于`string::npos` 的值

# C#

[C#嵌套类型](https://www.cnblogs.com/rinack/p/5695610.html)：类里声明类。  

struct是值类型，内存分配在栈上；  

Action与Func是特殊的delegate：func必须有返回值，可以加0到若干个参数，action必须没有返回值，可以加0到若干参数；用event修饰的delegate更加安全。  
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