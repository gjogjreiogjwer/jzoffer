# -*- coding:utf-8 -*-
'''
求1+2+3+…+n
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

example1:
输入: n = 3
输出: 6

example2:
输入: n = 9
输出: 45

解：采用递归。
'''

class Solution(object):
    
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        return n + self.sumNums(n-1)


if __name__ == '__main__':
    a = Solution()
    print (a.sumNums(9))