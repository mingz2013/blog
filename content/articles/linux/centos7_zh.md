Title: CentOS7 中文支持
Date: 2016-12-01 00:00
Modified: 2016-12-01 00:00
Category: Linux
Tags: CentOS7
Slug: centos7-zh
Author: Mingz
Summary: CentOS7 中文支持
Status:published

1. 查看系统版本信息
`cat /etc/redhat-release`
```
CentOS Linux release 7.1.1503 (Core)
```
`uname -m`
```
x86_64
```
`uname -r`
```
3.10.0-229.el7.x86_64
```
`uname -a`
```
Linux VM_7_30_centos 3.10.0-229.el7.x86_64 #1 SMP Fri Mar 6 11:36:42 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux
```

2. 当前文件配置
`cat /etc/locale.conf`
```
LANG="C"
```

3. 查看locale环境变量
`locale`
```
LANG=C
LC_CTYPE="C"
LC_NUMERIC="C"
LC_TIME="C"
LC_COLLATE="C"
LC_MONETARY="C"
LC_MESSAGES="C"
LC_PAPER="C"
LC_NAME="C"
LC_ADDRESS="C"
LC_TELEPHONE="C"
LC_MEASUREMENT="C"
LC_IDENTIFICATION="C"
LC_ALL=
```

4. 修改
`vim /etc/locale.conf`
```
#LANG="C"
LANG="zh_CN.UTF-8"
```

5. 重新登录
`exit`
`login`

6. 查看locale环境变量
`locale`
```
LANG=zh_CN.UTF-8
LC_CTYPE="zh_CN.UTF-8"
LC_NUMERIC="zh_CN.UTF-8"
LC_TIME="zh_CN.UTF-8"
LC_COLLATE="zh_CN.UTF-8"
LC_MONETARY="zh_CN.UTF-8"
LC_MESSAGES="zh_CN.UTF-8"
LC_PAPER="zh_CN.UTF-8"
LC_NAME="zh_CN.UTF-8"
LC_ADDRESS="zh_CN.UTF-8"
LC_TELEPHONE="zh_CN.UTF-8"
LC_MEASUREMENT="zh_CN.UTF-8"
LC_IDENTIFICATION="zh_CN.UTF-8"
LC_ALL=
```

7. 查看当前安装的中文语言包
`locale -a | grep zh`
```
zh_CN
zh_CN.gb18030
zh_CN.gb2312
zh_CN.gbk
zh_CN.utf8
zh_HK
zh_HK.big5hkscs
zh_HK.utf8
zh_SG
zh_SG.gb2312
zh_SG.gbk
zh_SG.utf8
zh_TW
zh_TW.big5
zh_TW.euctw
zh_TW.utf8
```
