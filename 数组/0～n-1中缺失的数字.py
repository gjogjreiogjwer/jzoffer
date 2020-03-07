# -*- coding:utf-8 -*-
'''
0～n-1中缺失的数字
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

example1:
输入: [0,1,3]
输出: 2

example2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8

解：二分法
如果中间数和索引相等，结果在右边
如果中间数和索引不相等，并且前面一个数和前一个数的索引也不相等，结果在左边
如果中间数和索引不相等，但是前面一个数和前面一个数的索引相等，中间数就是结果
'''

class Solution(object):
    def missingNumber(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] != mid:
                # 输入 [1], mid = 0, 输出 0
                if mid == 0 or nums[mid-1] == mid-1:
                    return mid
                else:
                    right = mid -1
            else:
                left = mid + 1
            # 结果是最右边
            if left == len(nums):
                return len(nums)


if __name__ == '__main__':
    a = Solution()
    print (a.missingNumber([0,1,2,3,4,5,6,7,9]))
















        			