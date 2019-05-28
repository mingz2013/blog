Title: Swarm
Date: 2019-05-28 12:00
Modified: 2019-05-28 12:00
Category: micros
Tags: micro service Swarm
Slug: swarm
Author: Mingz
Summary: Swarm
Status: published



# Docker Swarm

* Docker Machine 创建 Docker 主机
* Docker Swarm 配置集群节点
* Docker Service 部署单个集群服务
* Docker Stack 部署多个集群服务，以及 GUI 管理页面

* docker-machine、docker swarm、docker node、docker service 和 docker stack 常用命令



## Docker Machine

Docker Machine是Docker官方编排项目之一，是一个简化Docker安装的命令行工具，可以帮助用户构建拥有Docker运行环境的虚拟机，并能够远程管理虚拟机及其里面的容器。



## Docker Compose
Docker Compose是Docker的一种编排服务，是一个用于在Docker上定义并运行复杂应用的工具，可以让用户在集群中部署分布式应用。通过Compose，用户可以很容易的用一个配置文件定义一个多容器的应用，然后使用一条指令安装这个应用的所有依赖，完成构建。Docker Compose解决了容器与容器之间如何管理编排的问题，适合开发和测试环境。




## Docker Swarm

Swarm是Docker公司在2014年12月初发布的一套较为简单的工具，用来管理Docker集群，它将一群Docker宿主机变成一个单一的，虚拟的主机，使用Swarm操作集群，会使用户感觉就像是在一台主机上进行操作。Swarm使用标准的Docker API接口作为其前端访问入口，换言之，各种形式的Docker Client都可以直接与Swarm通信。

## Docker Node


## Docker Service



## Docker Stack



## 集群管理面板
- Shipyard
- Portainer
- Panamax
- Seagull






## 监控与日志
- cAdvisor 原生集群监控
- Logspout 日志处理
- Grafana  数据可视化



## 基于Docker的PaaS平台

- Deis 轻量级PaaS平台
- Tsuru 可扩展PaaS平台, 基于Swarm
- Flynn 模块化PaaS平台
- openshift



## Docker持续集成

- Drone 轻量级CI工具

- Travis CI 著名的CI/CD服务商









## 参考资料

### Books
- 《容器云运维实战：Docker与Kubernetes集群》







