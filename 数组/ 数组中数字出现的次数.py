# -*- coding:utf-8 -*-
'''
数组中数字出现的次数
1. 除了一个数字出现一次，其他都出现了两次，让我们找到出现一次的数

2. 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

example1:
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]

example2:
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

解：只出现一次的数系列： 位运算
1. 全员异或，出现两次的数异或自己为0

2. 目的：把只出现一次的数分别分入两个组，相同的数字要出现在同一组内，两个组各自做异或
把所有数字异或，结果肯定不为0，取其中为1的那位，把改位数和全员做异或，结果为0分一组，为1分一组
'''

class Solution(object):
    def singleNumbers1(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res


    def singleNumbers3(self, nums):
        res = 0
        a = 0
        b = 0
        for num in nums:
            res ^= num
        h = 1
        # 找到第一位不是0的
        while res & h == 0:
            h <<= 1
        for num in nums:
            # 根据该位是否为0分成两组
            if h & num == 0:
                a ^= num
            else:
                b ^= num
        return [a,b]



if __name__ == '__main__':
    a = Solution()
    print (a.singleNumbers1([1,2,3,3,2]))
    print (a.singleNumbers3([4,4,6,1]))










        			