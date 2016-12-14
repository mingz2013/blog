CentOS7 UTF8编码设置
############################

:date: 2016-12-01 00:00
:modified: 2016-12-14 12:00:00
:category: Linux
:tags: CentOS7
:slug: centos7-utf8-rst
:author: Mingz
:summary: CentOS7 utf8编码
:status: published

1. 查看系统版本信息
********************************
*$cat /etc/redhat-release*
::

    CentOS Linux release 7.1.1503 (Core)

*$uname -m*
::

        x86_64

*$uname -r*
::

    3.10.0-229.el7.x86_64

*$uname -a*
::

    Linux VM_7_30_centos 3.10.0-229.el7.x86_64 #1 SMP Fri Mar 6 11:36:42 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux

2. 当前文件配置
********************************
*$cat /etc/locale.conf*
::

    LANG="C"

3. 查看locale环境变量
********************************
*$locale*
::

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

4. 修改
********************************
*$vim /etc/locale.conf*
::

    #LANG="C"
    LANG="en_US.UTF-8"

5. 重新登录
********************************
*$exit*

*$login*

6. 查看locale环境变量
********************************
*$locale*
::

    LANG=en_US.UTF-8
    LC_CTYPE="en_US.UTF-8"
    LC_NUMERIC="en_US.UTF-8"
    LC_TIME="en_US.UTF-8"
    LC_COLLATE="en_US.UTF-8"
    LC_MONETARY="en_US.UTF-8"
    LC_MESSAGES="en_US.UTF-8"
    LC_PAPER="en_US.UTF-8"
    LC_NAME="en_US.UTF-8"
    LC_ADDRESS="en_US.UTF-8"
    LC_TELEPHONE="en_US.UTF-8"
    LC_MEASUREMENT="en_US.UTF-8"
    LC_IDENTIFICATION="en_US.UTF-8"
    LC_ALL=

7. 查看当前安装的语言包
********************************
*$locale -a | grep en_US*
::

    en_US
    en_US.iso88591
    en_US.iso885915
    en_US.utf8

