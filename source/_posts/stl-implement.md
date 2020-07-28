---
title: stl-implement
date: 2020-07-06 11:13:02
tags:
    - stl
    - C/C++
---

# 自己实现部分STL（Standard Template Library）

## 容器部分

### List

## 智能指针

### shared_ptr

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