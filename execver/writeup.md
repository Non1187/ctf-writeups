execver

题目类型：缓冲区溢出，敏感字符绕过

解题思路：`scanf`函数中的正则表达式在不匹配时会直接关闭标准输入并返回。但其**输入不受限**，因此可以直接输入覆盖`main`的返回地址。



Hint：最后输入时发昏了，直接用的objdump中的execv函数，后来多次尝试的时候发现了，改成了ida中的plt地址，正确了。