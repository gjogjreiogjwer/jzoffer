# -*- coding:utf-8 -*-
'''
扑克牌顺子
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

example1:
输入: [1,2,3,4,5]
输出: True

example2:
输入: [0,0,1,2,5]
输出: True

解： 输入5个数；在0-13之间；除大小王外无重复；大小差值<=5
'''

class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) != 5:
            return False
        flag = 0
        maximum = -1
        minimum = 14
        for num in nums:
            if num > 13 or num < 0:
                return False
            # 大小王
            if num == 0:
                continue
            # 是否重复，重点
            if flag >> num & 1 == 1:
                return False
            flag |= 1 << num
            if num > maximum:
                maximum = num
            if num < minimum:
                minimum = num
            if maximum - minimum >= 5:
                return False
        return True

if __name__ == '__main__':
    a = Solution()
    print (a.isStraight([1,2,0,3,5]))