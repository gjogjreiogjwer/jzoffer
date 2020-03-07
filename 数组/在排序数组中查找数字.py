# -*- coding:utf-8 -*-
'''
在排序数组中查找数字
统计一个数字在排序数组中出现的次数。

example1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

example2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

解：字典
'''

class Solution(object):
    def search(self, nums, target):
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        if target in nums:
            return dict[target]
        else:
            return 0

if __name__ == '__main__':
    a = Solution()
    print (a.search([5,7,7,8,8,10], 8))


















        			