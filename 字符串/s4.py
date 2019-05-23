# -*- coding:utf-8 -*-
# 左旋转字符串
# 汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
# 对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
# 例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
# 解：把字符串转化为列表。

class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if len(s) <= 0:
            return ''
        s_list = list(s)
        for i in range(n):
            s_list.append(s_list.pop(0))
        return ''.join(s_list)

if __name__=='__main__':
	b = Solution()
	print (b.LeftRotateString('asdfg', 2))
