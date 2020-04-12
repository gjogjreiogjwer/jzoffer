# -*- coding:utf-8 -*-
'''
数组中重复的数字
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

example:
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 

解1：0（索引值）和2（索引值位置元素）不相等，并且2和以2为索引值的1也不想等，交换2，1，得[1,3,2,0,2,5,3]
   0（索引值）和1（索引值位置元素）不相等，并且1和以1为索引值的3也不想等，交换1，3，得[3,1,2,0,2,5,3]
   0（索引值）和3（索引值位置元素）不相等，并且3和以3为索引值的0也不想等，交换3，0，得[0,1,2,3,2,5,3]
   0（索引值）和0（索引值位置元素）相等，遍历下一个元素
   该方法只适用于范围0-n-1
'''

class Solution:
    # 解法1更快
    def findRepeatNumber(self, numbers):
        # write code here
        n = len(numbers)
        for i in range(n):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    return numbers[i]
                # 注意不能反着写，先numbers[numbers[i]]，再修改numbers[i]
                numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]


    # 解法2
    # 位运算，首次出现的数就在该位上为1. e.g. 4: 1000
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for num in nums:
            if x >> num & 1 == 1:
                return num
            x |= 1 << num


if __name__ == '__main__':
    a = Solution()
    print (a.findRepeatNumber([2,3,1,0,2,5,3]))