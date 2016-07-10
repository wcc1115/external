# Ovirt外部调度器

使用oVirt外部调度器实现自己的调的策略.

## 进展

- 2016-07-10
    - 源代码已经处于maven的管理之下
    - 初步完成了对外部调度模块的简单分离

## 计划

- 对"离线外部调度器"进行调试
- 逐步引入并测试以下方法:
    - *ExternalSchedulerBrokerImpl*.runDiscover()
    - *ExternalSchedulerDiscoveryResult*.populate()
    - *ExternalSchedulerBrokerImpl".{runFilters, runScores, runBalance}()
- 外部调度策略的保存与使用过程
- 外部调度器的配置与ovirt插件

## 文件说明

- external/ 外部调度器的工程目录(maven3)
- README.md 项目说明文件
