# -*- coding:utf-8 -*-
'''
数值的整数次方
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

example1:
输入: 2.00000, 10
输出: 1024.00000

example2:
输入: 2.10000, 3
输出: 9.26100

example3:
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25

解：考虑指数为负.
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n:
            # n % 2 == 1
            if n & 1:
                res *= x
            x *= x
            # 向右移一位相当于 n//2
            n >>= 1
        return res



if __name__ == '__main__':
    a = Solution()
    print (a.myPow(2,3))