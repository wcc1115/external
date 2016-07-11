# Ovirt外部调度器

使用oVirt外部调度器实现自己的调的策略.

## 进展

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

- 引入以下类以完成对populate()的调试:
    - StringUtiles
    - SimpleCustomPropertiesUtil
    - ExternalSchedulerDiscoveryUnit

### 总计划

- 逐步引入并测试以下方法:
    - *ExternalSchedulerDiscoveryResult*.populate()
    - *ExternalSchedulerBrokerImpl*.{runFilters, runScores, runBalance}()
- 外部调度策略的保存与使用过程
- 外部调度器的配置与ovirt插件

## 文件说明

- external/ 外部调度器的工程目录, 使用maven3管理
- xmlrpc-server/ xmlrpc服务器目录
- README.md 项目说明文件
