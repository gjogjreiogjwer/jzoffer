# -*- coding:utf-8 -*-
'''
剪绳子
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 
可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，
此时得到的最大乘积是18。

example1:
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

example2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

解：
贪心
'''

import math

class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        # m>1必须要剪
        if n <= 3:
            return n - 1
        x = n % 3
        y = n // 3
        if x == 0:
            return int(math.pow(3, y))
        elif x == 1:
            return int(math.pow(3, y-1) * 4)
        else:
            return int(math.pow(3, y) * 2)

if __name__ == '__main__':
    a = Solution()
    print (a.cuttingRope(10))