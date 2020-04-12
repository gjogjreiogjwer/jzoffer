# -*- coding:utf-8 -*-
'''
剪绳子2
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

example1:
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

example2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

解：
大数越界： 当 a 增大时，最后返回的 3^a大小以指数级别增长，可能超出 int32 甚至 int64 的取值范围，导致返回值错误。
快速幂求余，具体看 数值的整数次方
'''

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
        y = n // 3 - 1
        r = 1
        k = 3
        while y:
            if y % 2:
                r = (r * k) % 1000000007
            k = k ** 2
            y //= 2
        if x == 0:
            return (r * 3) % 1000000007
        elif x == 1:
            return (r * 4) % 1000000007
        else:
            return (r * 6) % 1000000007



if __name__ == '__main__':
    a = Solution()
    # print (a.cuttingRope(10))
    print (a.cuttingRope(10))