# Ovirt外部调度器

使用oVirt外部调度器实现自己的调的策略

## 进展

- 2016-07-19
    - runBalance()和runScore()调试通过
    - 现在服务器可以在终端打印日志了
    - 对rpc server代码进行了少许的函数抽象与封装

- 2016-07-18
    - 了解了依赖注入和控制反转, 试图理解@Inject的工作过程但是失败了
    - 了解了balance和filter & score的关系
    - 了解了runBalance(), runFilters(), runScores()的调用栈

- 2016-07-17
    - 理解了以下过程:
        - 外部调度器发现,固化,访问
        - 外部过滤器RPC的方法,参数以及返回值
    - runFilters()方法调试通过

- 2016-07-16
    - *ExternalSchedulerDiscoveryResult*.populate()调试通过
    - *ExternalSchedulerBroker*.runDiscover()调试通过
    - 外部调度器发现过程调试通过

- 2016-07-11
    - 已经配置好了简单的xml-rpc服务器 
    - 搭建了简单的JUnit测试框架
    - ExternalSchedulerBrober.runDiscover()已经可以连接到服务器了
    - ExternalSchedulerDiscoveryResult.populate()函数测试中...

- 2016-07-10
    - 源代码已经处于maven的管理之下
    - 初步完成了对外部调度模块的简单分离

## 计划

### 近期计划

- xml-rpc服务器重构
- 消化已通过的4个RPC函数,离线调度器的调试做准备
    - 传递给3个调度函数的参数与runDiscover()函数返回值的关系
    - 特别地,properties参数该怎么使用?
    - 整个外部调度器的详细(代码级)工作过程是什么样的?
- 着手上机实验
    - 离线调度器上机实验
    - 外部调度器配置:开关,RPC设置
    - 简单的运行调试
    - 算法调试

### 已完成计划

- runScores()和runBalance()方法调试
- 跟踪外部调度单元固化过程
- 跟踪外部调度单元访问过程
- runFilters()调试
- 引入以下类以完成对populate()的调试:
    - StringUtiles
    - SimpleCustomPropertiesUtil
    - ExternalSchedulerDiscoveryUnit

### 总计划

- 逐步引入并测试以下方法(**已完成**):
    - *ExternalSchedulerDiscoveryResult*.populate()
    - *ExternalSchedulerBrokerImpl*.{runFilters, runScores, runBalance}()
- 外部调度策略的保存与使用过程(**已完成**):
- 离线线调度器调式(**进行中**)
- 外部调度器的配置与ovirt插件

## 文件说明

- external/ : 外部调度器的工程目录, 使用maven3管理
- xmlrpc-server/ : xmlrpc服务器目录
- README.md :
