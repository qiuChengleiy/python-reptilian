# python-reptilian
python 爬虫学习笔记 本项目适合有python基础的同学~~ 

### 什么是爬虫

爬虫，即网络爬虫，大家可以理解为在网络上爬行的一直蜘蛛，互联网就比作一张大网，而爬虫便是在这张网上爬来爬去的蜘蛛咯，如果它遇到资源，那么它就会抓取下来。想抓取什么？这个由你来控制。

比如它在抓取一个网页，在这个网中他发现了一条道路，其实就是指向网页的超链接，那么它就可以爬到另一张网上来获取数据。这样，整个连在一起的大网对这之蜘蛛来说触手可及，分分钟爬下来不是事儿。

### Urllib库的使用

* 扒网页

```py

import urllib2
 
response = urllib2.urlopen("http://www.baidu.com")
print response.read();


```

* 最终在终端输出如下：  你会看到如下完整的html源码

![]('');

##### 方法

* urlopen(url, data, timeout);

从字面上看三个参数也能猜出: url就是URL(必需) data访问url传的数据 timeout超时

 第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT

*  response.read() 

返回网络数据 就是我们刚刚读到的网页内容

写的时候建议加上 request对象

```py
import urllib2
 
request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()
```

























