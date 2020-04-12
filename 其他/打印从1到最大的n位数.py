# -*- coding:utf-8 -*-
'''
打印从1到最大的n位数
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

example1:
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]

'''
import math
class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        maxNum = int(math.pow(10, n))
        r = []
        for i in range(1, maxNum):
            r.append(i)
        return r

if __name__ == '__main__':
    a = Solution()
    print (a.printNumbers(2))