# -*- coding:utf-8 -*-
'''
数组中数字出现的次数
除了一个数字出现一次，其他都出现了三次，让我们找到出现一次的数。

example1:
输入：nums = [3,4,3,3]
输出：4

example2:
输入：nums = [9,1,7,9,7,9,7]
输出：1

解：利用位运算
'''

class Solution(object):
    def singleNumbers(self, nums):
        res = 0
        for i in range(32):
            # h代表需要判断的第几位
            h = 1 << i
            count = 0
            for num in nums:
                # !=0 表示这位上二进制为1, e.g. 2&3=2，
                # 注意：不能写if num & h == 1
                if num & h != 0:
                    count += 1
            # count = 0 表示这位上所有数都是0，count = 3的倍数 表示这位上有3的倍数个为1
            if count % 3 != 0:
                # 唯一出现的数在这位上为1
                res |= h
        return res


if __name__ == '__main__':
    a = Solution()
    print (a.singleNumbers([1,2,3,3,2,2,3]))










        			