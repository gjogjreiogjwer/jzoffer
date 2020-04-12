# -*- coding:utf-8 -*-
'''
和为S的两个数字
输入一个递增排序的数组和一个数字s，
在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

example1:
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

example2:
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]

解：两个指针分别遍历一边数组，一个从右往左，一个从左往右。
    两个指针指向的数字和等于target，输出
    两个指针指向的数字和大于target，右指针往左移一格
    两个指针指向的数字和小于target，左指针往右移一格
    这样还能保证这两个数乘积最小
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [nums[left], nums[right]]
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return []


if __name__ == '__main__':
    a = Solution()
    print (a.twoSum([2,7,11,15], 9))

