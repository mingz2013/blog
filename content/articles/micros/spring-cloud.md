Title: Spring Cloud
Date: 2019-05-23 12:00
Modified: 2019-05-23 12:00
Category: micros
Tags: Spring Cloud, micro service
Slug: spring-cloud
Author: Mingz
Summary: spring cloud
Status: published



# SpringCloud




## 概念



Spring Cloud最早在功能层面为微服务治理定义了一系列标准特性，例如智能路由，熔断机制，服务注册与发现等，并提供了对应的库和组件来实现这些标准特性。到目前为止，这些库和组件被广泛采用。

Spring Cloud缺点：

- 既博采众家之长，也导致了一些散乱的局面，即用户需要学习和熟悉各组件的”方言“并加以运维，这在客观上提高了应用门槛
- 需要在代码级别对诸多组件进行控制，包括Sidecar在内的组件都依赖Java的实现，这和微服务的多语言协作目标是背道而驰的
- 自身并没有对调度，资源，DevOps等提供相关支持，需要借助其他平台来完成，然而目前的容器编排事实标准是k8s，二者的部分功能存在重合或者冲突，这在一定程度上影响了Spring Cloud的长远发展。




