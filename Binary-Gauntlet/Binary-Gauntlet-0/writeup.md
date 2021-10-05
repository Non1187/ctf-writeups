Binary-Gauntlet-0

保护机制：ASLR

绕过方法：ROP绕过，利用`jmp esp`及`asm('sub esp,0x**;jmp esp')`运行shellcode。



Hint：64位程序使用pattern offset方法时似乎要直接从栈顶取ret值再分析

​			调用asm时，64位程序对应的寄存器形如rsi。

​			在32位与64位程序中需要使用不同的shellcode。



参考资料：[(1条消息) 其它栈溢出技巧_听鬼哥说故事-CSDN博客](https://blog.csdn.net/guiguzi1110/article/details/77663874)