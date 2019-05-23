Title: ollvm
Date: 2018-10-11 11:30
Modified: 2018-10-11 11:30
Category: compiler
Tags: compiler, llvm, ollvm
Slug: compiler-ollvm
Author: Mingz
Summary: 由解决ios 4.3过审问题引发的探讨
Status: published



# 做的事情
- 之前已经做的东西，资源加密，符号混淆
- 本次做的事情，代码膨胀，变形


# 名词介绍

## gcc

GNU编译器套件（GNU Compiler Collection）包括C、C++、Objective-C、Fortran、Java、Ada和Go语言的前端，也包括了这些语言的库（如libstdc++、libgcj等等）。GCC的初衷是为GNU操作系统专门编写的一款编译器。GNU系统是彻底的自由软件。此处，“自由”的含义是它尊重用户的自由。


## llvm
LLVM是构架编译器(compiler)的框架系统，以C++编写而成，用于优化以任意程序语言编写的程序的编译时间(compile-time)、链接时间(link-time)、运行时间(run-time)以及空闲时间(idle-time)，对开发者保持开放，并兼容已有脚本。


## clang
Clang是一个C语言、C++、Objective-C语言的轻量级编译器。源代码发布于BSD协议下。Clang将支持其普通lambda表达式、返回类型的简化处理以及更好的处理constexpr关键字。


## ollvm
OLLVM（Obfuscator-LLVM）是瑞士西北应用科技大学安全实验室于2010年6月份发起的一个项目，这个项目的目标是提供一个LLVM编译套件的开源分支，能够通过代码混淆和防篡改，增加对逆向工程的难度，提供更高的软件安全性。目前，OLLVM已经支持LLVM-4.0.1版本。OLLVM的混淆操作就是在中间表示IR层，通过编写Pass来混淆IR，然后后端依据IR来生成的目标代码也就被混淆了。得益于LLVM的设计，OLLVM适用LLVM支持的所有语言（C, C++, Objective-C, Ada 和 Fortran）和目标平台（x86, x86-64, PowerPC, PowerPC-64, ARM, Thumb, SPARC, Alpha, CellSPU,MIPS, MSP430, SystemZ, 和 XCore）



# llvm相关架构与原理

https://llvm.org/docs/

http://www.aosabook.org/en/llvm.html


https://llvm.org/docs/WritingAnLLVMPass.html

# ollvm扩展内容


https://github.com/obfuscator-llvm/obfuscator/wiki





1.     -fla 控制流扁平化的PASS参数

2.     -sub指令替换的PASS参数

3.     -bcf虚假控制流的PASS参数



https://blog.csdn.net/chrisnotfound/article/details/79026449




# demo
用Armariris演示编译一个简单的C源码，试用各种参数。

对编译出的二进制进行分析，查看文件大小，用ida分析二进制，展示流图。


# 攻与防

https://bbs.pediy.com/thread-217727.htm

http://www.freebuf.com/articles/terminal/130142.html






# github

- [llvm](https://github.com/llvm-mirror/llvm)
- [ollvm](https://github.com/obfuscator-llvm/obfuscator)
- [Hikari](https://github.com/HikariObfuscator/Hikari)
- [Armariris](https://github.com/GoSSIP-SJTU/Armariris)
- [mcsema](https://github.com/trailofbits/mcsema)



# 参考书籍
- 《iOS应用逆向与安全》
- 《编译与反编译技术实战》
- 《LLVM Cookbook中文版》


# links
- [gcc](https://www.gnu.org/software/gcc/)
- [clang](http://clang.llvm.org/)
- [LLVM和GCC的区别](https://www.cnblogs.com/zuopeng/p/4141467.html)
