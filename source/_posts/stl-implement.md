---
title: stl-implements && code practices
date: 2020-07-06 11:13:02
tags:
    - stl
    - C/C++
    - 智能指针
    - 多线程
---

# 自己实现部分STL（Standard Template Library）

## 容器部分

### List

## 智能指针

### SharedPtr ver1

``` C++
// mysharedptr.h

#pragma once
using namespace std;

template<class T>
class MySharedPtr
{
public:
	MySharedPtr(T* _p);
	MySharedPtr(const MySharedPtr& r);
	MySharedPtr& operator=(const MySharedPtr& r);
	T operator*();
	~MySharedPtr();
	int use_count();

private:
	T* p;
	int* count;
};
```

``` C++
// mysharedptr.cpp

#include "mysharedptr.h"
#include <iostream>
using namespace std;

template<class T>
MySharedPtr<T>::MySharedPtr(T* _p):p(_p){
	cout << "constructor" << endl;
	count = new int(0);
	if (p != nullptr)
		*count = 1;
}
template MySharedPtr<int>::MySharedPtr(int* _p); // declaration和definition如果不放在一起的写法，这里只用到了构造和析构，如果用别的方法也应该加上这个声明

template<class T>
MySharedPtr<T>::MySharedPtr(const MySharedPtr& r) {
	cout << "copy constructor" << endl;
	p = r.p;
	count = r.count;
	*r.count++;
}

template<class T>
MySharedPtr<T>& MySharedPtr<T>::operator=(const MySharedPtr& r) {
	if (-- * count == 0) {
		delete p;
		delete count;
	}
	p = r.p;
	count = r.count;
	*r.count++;
	return *this;
}

template<class T>
T MySharedPtr<T>::operator*() {
	return *p;
}

template<class T>
MySharedPtr<T>::~MySharedPtr(){
	if (-- * count == 0) {
		delete p;
		delete count;
	}
}

template MySharedPtr<int>::~MySharedPtr(); // declaration和definition如果不放在一起的写法

template<class T>
int MySharedPtr<T>::use_count() {
	return *count;
}
```
类模板的声明和定义应该放在一起，这里是不放在一起的写法


### SharedPtr ver2

``` C++
template<class T>
class SharedPtr
{
public:
	SharedPtr();
    SharedPtr(T* p);
    SharedPtr(SharedPtr& sp);
	~SharedPtr();

    SharedPtr& operator= (const SharedPtr& sp);
    int use_count();

private:
    T* p;
    int* refCount;
};

template<class T>
SharedPtr<T>::SharedPtr():p(nullptr),refCount(new int(0))
{
}

template<class T>
SharedPtr<T>::SharedPtr(T* _p) : p(_p), refCount(new int(1))
{
}

template<class T>
SharedPtr<T>::SharedPtr(SharedPtr& sp) : p(sp.p), refCount(&(++*(sp.refCount)))
{
}

template<class T>
SharedPtr<T>::~SharedPtr()
{
    if (p && --*refCount == 0) {
        delete p;
        delete refCount;
    }
}

template<class T>
SharedPtr<T>& SharedPtr<T>::operator= (const SharedPtr& other) {
    if (this == &other)
        return *this;

    ++* other.refCount;
    if (-- * refCount == 0) {
        delete p;
        delete refCount;
    }

    p = other.p;
    refCount = other.refCount;
    return *this;
}

template<class T>
int SharedPtr<T>::use_count(){
    return *refCount;
}


int main() {
    int* p = new int(3);
    SharedPtr<int> sp(p);
    SharedPtr<int> ssp(p);
    SharedPtr<int> sssp(sp);
    cout << sp.use_count() << " " << ssp.use_count() << " " << sssp.use_count() << endl;
	// output: 2 1 2
    return 0;
}

```


## C++11多线程

[参考资料](https://www.cnblogs.com/DOMLX/p/10945309.html)
[参考资料2](https://zhuanlan.zhihu.com/p/77999255)
[参考资料3](https://www.jianshu.com/u/88ad4f76eb79)