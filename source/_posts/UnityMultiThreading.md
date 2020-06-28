---
title: Unity中的多线程与线程池应用
date: 2020-06-05 13:00:19
tags:
    - Unity
    - 多线程
    - 线程池
---

# Part 1 Unity中的多线程

* FileStream读取本地文件
``` C#
byte[] buffer;
void LoadFiletoBuffer()
{
    // 假如很卡
    Thread.Sleep(3000);
    // 通过路径加载本地图片
    FileStream fs = new FileStream("C:\\Users\\Administrator\\Downloads\\pic.jpg", FileMode.Open);
    buffer = new byte[fs.Length];
    fs.Read(buffer, 0, buffer.Length);
    fs.Close();
}
```

* buffer-->Unity texture2d-->Unity sprite，使用UnityEngine中组件的动作必须在主线程完成，所以这段逻辑不能放到LoadFiletoBuffer中
这里使用协程的目的是异步（在buffer加载进来之后）创建texture以及sprite
``` C#
IEnumerator OnLoad()
{
    while (buffer == null)
    {
        yield return 0;
    }
    Debug.Log("load tex");

    Texture2D tex = new Texture2D(2, 2);
    var iSLoad = tex.LoadImage(buffer);
    tex.Apply();
    if (!iSLoad)
    {
        Debug.Log("Texture存在但生成Texture失败!");
    }

    img.sprite = Sprite.Create(tex, new Rect(0, 0, 5939, 3341), Vector2.zero);
}
```

* 最外层接口，两种方法的区别在于load file这3000ms主线程是否卡死
``` C#
/// <summary>
/// 文件流加载图片
/// </summary>
void FileStreamLoadTexture()
{
    // load file by sub thread
    Thread childThread = new Thread(new ThreadStart(LoadFiletoBuffer));
    childThread.Start();

    //// load file by main thread
    //LoadFiletoBuffer();

    Debug.Log("start coroutine");
    StartCoroutine("OnLoad");
    Debug.Log("end coroutine");
}
```

# Part 2 线程池

C# System.Threading.ThreadPool类提供了线程池的实现，都是静态方法，不需要实例化  
PS： CLR指公共语言运行时(Common Language Runtime)  
线程池初始化时是没有线程的，线程池里的线程的初始化与其他线程一样，但是在完成任务以后，该线程不会自行销毁，而是以挂起的状态返回到线程池。直到应用程序再次向线程池发出请求时，线程池里挂起的线程就会再度激活执行任务。  

[参考资料](https://www.cnblogs.com/scmail81/archive/2018/08/19/9503266.html)

``` C#
/// <summary>
/// 文件流加载图片
/// </summary>
void FileStreamLoadTexture()
{
    //// load file by sub thread
    //Thread childThread = new Thread(new ThreadStart(LoadFiletoBuffer));
    //childThread.Start();

    // use thread pool
    ThreadPool.GetAvailableThreads(out int workerThreads, out int completionProtThreads); // 800 200；out/ref的区别：out不需要初始化
    Debug.Log("Thread Pool1: " + workerThreads + " " + completionProtThreads);

    ThreadPool.QueueUserWorkItem(new WaitCallback(LoadFiletoBuffer), null);

    //// load file by main thread
    //LoadFiletoBuffer();

    Debug.Log("start coroutine");
    StartCoroutine("OnLoad");
    Debug.Log("end coroutine");
}
```

# part 3 C#中的async和await

属于System.Threading.Task，async/await Task是C#中更先进的，也是微软大力推广的特性，我们在开发中可以尝试使用Task来替代Thread/ThreadPool，处理本地IO和网络IO任务是尽量使用async/await来提高任务执行效率。  
await后边是个异步方法，也就是说async自定义的异步方法中有一个或者多个await，每个await后边还是一个返回值为
* Task\<T>（返回值为T类型）
* Task（没有返回值，但是可以查看异步调用的状态）
* void（调用完就不关心了，没有互动了）的异步方法

最底层这个异步方法往往来自BCL（C#的基础类库，例如WebClient.DownloadStringTaskAsync(url)）  

``` C#
async Task<int> CountCharactersAsync(int id, string site){
    Console.WriteLine("starting countingcharacters");
    WebClient wc = new WebClient();

    string result = await wc.DownloadStringTaskAsync(new Uri(site));

    Console.WriteLine("countingcharacters completed");
    return result.Length;
}
```

20.3.5 Wait()/WaitAll()/WaitAny()  
20.10 BeginInvoke()和EndInvoke()  
——《C#图解教程》