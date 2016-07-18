# 笔记

- org.apache.commons.lang -> org.apache.commons.lang3

- 外部调度单单元
    - (名字,描述,属性),名字是键,[描述,属性]是值
    - 属性格式:key=value, 或者:key1=value1;key2=value2;...;keyn=valuen

- runFilters返回值格式见服务器

- balance()和filter() & score()的关系:
    - balance()给出一个VM和一组主机
    - filter()&score()从中选择最优主机

- 调用栈
    - schedule()
        - runFilters()
            - runExternalFilter()
                - ExternalSchedulerFactory.getInstance().runFilters()
        - selectBestHost()
            - runFunctions()
                - runExternalFunctions()
                    - ExternalSchedulerFactory.getInstance().runScores()
    - performLoadBalancing()
        - externalRunBalance()
            - ExternalSchedulerFactory.getInstance().runBalance()
