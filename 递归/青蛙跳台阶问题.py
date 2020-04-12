# -*- coding:utf-8 -*-
'''
跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

example1:
输入：n = 2
输出：2

example2:
输入：n = 7
输出：21

解：1,2,3,5...裴波那契数列。
'''

class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n <= 3:
            return n
        first = 2
        second = 3
        for i in range(4, n+1):
            third = first + second
            first = second
            second = third
        return third % 1000000007

if __name__ == '__main__':
    a = Solution()
    print (a.numWays(6))