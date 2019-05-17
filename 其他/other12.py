# -*- coding:utf-8 -*-
# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
# 解： a：不算进位,b：进位值。结束条件：进位值为0
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
        	a=num1^num2
        	b=(num1&num2)<<1
        	num1=a
        	num2=b
        return a

if __name__ == '__main__':
	b=Solution()
	print b.Add(5,7)