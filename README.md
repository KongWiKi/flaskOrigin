## flask源码解读

这是一个佛系的仓库 :stuck_out_tongue_winking_eye:  :stuck_out_tongue_winking_eye:，不定期的更新，慢慢的看源码，慢慢的写笔记 :pig_nose: ​ :pig_nose:。

~~**开更 9021/09/24**~~

## 添加0.1版本源码



## WSGI

由WSGI的规定，web程序(WSGI程序)必须是一个可调用的对象(callable object)，并且其包含了如下的两个参数：

* environ
  * 请求中的所有信息的字典
* start_response
  * 需要在可调用对象中调用的函数，用来发起响应，参数是状态码、响应头部等

## 设计理念

#### 微框架

#### 两个核心依赖

1. **Werkzeug**
   1. 负责核心的逻辑模块如路由、请求和应答
2. **Jinja**
   1. 负责模板渲染

#### 三种程序状态

* 程序设置状态(applilcation setup state)
* 程序运行状态(application runtime state)
* 请求运行状态(request runtime state)



