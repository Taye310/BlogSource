---
title: C++中的设计模式
date: 2020-06-14 15:39:46
tags:
    - 设计模式
    - C++
    - 单例模式
    - 命令模式
---

# 1.单例模式

下面的代码为C++中单例模式的实现，需要注意的是instance的初始化，这是因为类的成员变量在使用前必须先初始化。
懒汉模式：

``` C++
class Singleton {
private:
	static Singleton* instance;
	Singleton() {};
public:
	static Singleton* GetInstance();
	void func();
};

Singleton* Singleton::GetInstance() {
	if (!instance) {
		instance = new Singleton();
	}
	return instance;
}

void Singleton::func() {
	cout << "hello" << endl;
}

Singleton* Singleton::instance = nullptr; // 记得初始化

int main() {
	Singleton* ins = Singleton::GetInstance();
	ins->func();
	return 0;
}
```

为了避免多线程创建出多个instance实例（C++的new非线程安全），应使用饿汉模式：
``` C++
class Singleton {
private:
	static Singleton* instance;
	Singleton() {};
public:
	static Singleton* GetInstance();
	void func();
};

Singleton* Singleton::GetInstance() {
    // 不再需要判空创建
	return instance;
}

void Singleton::func() {
	cout << "hello" << endl;
}

Singleton* Singleton::instance = new Singleton(); // 最开始就初始化实例

int main() {
	Singleton* ins = Singleton::GetInstance();
	ins->func();
	return 0;
}
```


# 2.命令模式

``` C++
class Command
{
public:
	string name;
	virtual void Execute() {
		cout << "execute:" << name << endl;
	}

	void Recall() {
		cout << "recall:" << name << endl;
	}
};

class AddCommand : public Command {
public:
	virtual void Execute() {
		cout << "addcommand execute" << endl;
	}

	void Recall() {
		cout << "addcommand recall" << endl;
	}
};

class CommandManager {
public:
	void Do(Command c) {
		c.Execute();
		if (dq.size() == capacity) dq.pop_front();
		dq.push_back(c);
	}

	void Undo() {
		Command tmp = dq.back();
		tmp.Recall();
		dq.pop_back();
	}

	void Redo() {

	}
private:
	int capacity = 10;
	deque<Command> dq;
};


int main() {
	Command* cp = new AddCommand();
	cp->name = "ac";
	cp->Execute();
	cp->Recall();
	return 0;
}
```