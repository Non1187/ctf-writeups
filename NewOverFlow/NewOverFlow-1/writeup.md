NewOverFlow-1

题目类型：64位栈溢出

解题思路：题目说是非常简单的64位栈溢出，但是本地能过，远程服务器总是出错。

一开始以为是接收的问题，想了一天。

最终尝试在网上查找，发现这题是picoCTF的原题。。。问题在于本地和服务器端的编译器版本不同，对于服务器端的编译器版本来说`movaps`命令的操作数地址必须是16byte对齐的。而本题中调用`main()`一次将导致`rsp+0x50`值为`0x7fff815c94a8`，没有对齐，引发了`general-protection exception`。

最终的解决方案为调用`main`函数两次再调用`flag`。这里应该是假设在调用栈中，`main`前后均为16字节对齐，而`main`本身导致了8字节的偏移，并且很幸运的是结果就是如此。



Hint：可以看一下参考资料中的分析过程，作者是在可以登录`server`端的前提下分析了core文件，用gdb进行调试得到的结果。展现了gdb比较强大的功能。

参考资料：[CTFs/NewOverFlow-1.md at master · Dvd848/CTFs · GitHub](https://github.com/Dvd848/CTFs/blob/master/2019_picoCTF/NewOverFlow-1.md)