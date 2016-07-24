# Ovirt外部调度器

使用oVirt外部调度器实现自己的调的策略

## 进展
- 2016-07-24 完成了以下工作:
    - xml-rpc目录树的设计与实现
    - 外部调度器架构的设计与实现
    - 目录结构与包结构的设计与实现,
    - 简单的过滤器"noop_filter",评分器"noop_score",平衡器"nooop_balance"的设计,实现与测试
    - 调度策略单元装载器"loader"模块的设计,实现与测试
    - rpc函数服务"service"模块的设计,实现与测试
    - ovirt rest api通信接口"ovirtapi"模块的设计,实现,与测试
    - 外部调度服务器"extschserver"模块的设计,实现与测试

- 2016-07-23
    - 尝试重构了server代码
    - 引入ovirtsdk实现了简单的filter
    - 研究了一下用java重写xmlrpc服务器的可能性

- 2016-07-22
    - ovirt外部调度器开发环境已经基本搭建完成了
        - 外部调度器已经配置好了
        - ovirt已经可以连接到外部调度器了
        - ovirt已经可以成功发现并装载外部调度策略了
        - 用户已经可以编辑,配置,使用外部调度策略了
    - 理解了以下内容
        - 外部调度器的配置方式以及参数意义
        - RPC函数的全部参数意义
        - RPC函数的实用过程
        - RPC函数在前端的展现形式以及配置方式

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

- 各种文档,注释以及README文件的编写
- 上述算法的在线调试
- 节能算法的实现与调试

### 总计划

- 逐步引入并测试以下方法(**已完成**):
    - *ExternalSchedulerDiscoveryResult*.populate()
    - *ExternalSchedulerBrokerImpl*.{runFilters, runScores, runBalance}()
- 外部调度策略的保存与使用过程(**已完成**):
- 离线线调度器调式(**进行中**)
- 在线调度器调试
- 外部调度器的配置与ovirt插件(**已完成**)

## 文件说明

- external/ : 外部调度器的工程目录, 使用maven3管理
- xmlrpc-server/ : xmlrpc服务器目录
- README.md :
