# -*- coding:utf-8 -*-
'''
不用加减乘除的加法
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

example:
输入: a = 1, b = 1
输出: 2
解：二进制每位相加相当于做异或；进位值是做与并左移一位。 
   a：不算进位,b：进位值。结束条件：进位值为0.
'''

class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 如果存在负数则需要转换成补码的形式,正数补码是他本身
        a &= 0xffffffff
        b &= 0xffffffff
        while b:
            x = a ^ b
            #如果是负数,转换成补码形式
            y = ((a & b) << 1) & 0xffffffff
            a = x
            b = y
        #如果是正数的话直接返回
        if a < 0x80000000:
            return a
        #是负数的话,转化成其原码
        else:
            return ~(a^0xffffffff)

if __name__ == '__main__':
    a = Solution()
    print (a.add(-3,4))