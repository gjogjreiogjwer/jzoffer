# -*- coding:utf-8 -*-
'''
调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

example:
输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。

'''

class Solution(object):
    # insert()，弹出一位补在开头，对i没影响
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        for i in range(len(nums)):
            if nums[i] & 1:
                nums.insert(0, nums.pop(i))
        return nums


    # 首尾指针
    # 左指针右移直到偶数
    # 右指针左移直到奇数
    def exchange1(self, nums):
        if not nums:
            return []
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] & 1:
                left += 1
                continue
            if not nums[right] & 1:
                right -= 1
                continue
            nums[left], nums[right] = nums[right], nums[left]
        return nums


    # 快慢指针
    # fast的作用是向前搜索奇数位置，low的作用是指向下一个奇数应当存放的位置
    def exchange2(self, nums):
        fast = 0
        low = 0
        while fast < len(nums):
            if nums[fast] & 1:
                nums[fast], nums[low] = nums[low], nums[fast]
                low += 1
            fast += 1
        return nums



if __name__ == '__main__':
    a = Solution()
    print (a.exchange2([1,3,5]))












