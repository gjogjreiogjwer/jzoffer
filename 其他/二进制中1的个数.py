# -*- coding:utf-8 -*-
'''
二进制中1的个数
请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。
因此，如果输入 9，则该函数输出 2。

解：一个数减去1后,该数最右边为1开始的所有位都取反
与上它本身，会把这个数最右边的1变0.
1100&1011=1000
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            n &= 0xffffffff
        count = 0
        while n:
            n &= (n-1)
            count += 1
        return count


    def hammingWeight1(self, n):
        count = 0
        for i in range(32):
            count += ((n >> i) & 1)
        return count

if __name__ == '__main__':
    a = Solution()
    print (a.hammingWeight1(12))