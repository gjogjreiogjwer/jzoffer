# -*- coding:utf-8 -*-
'''
旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，
数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

example1:
输入：[3,4,5,1,2]
输出：1

example2:
输入：[2,2,2,0,1]
输出：0

解：采用二分法。设置两个指针，分别指向头尾。
   若中间元素大于第一个指针，即它位于前面的递增数组，更新第一指针指向中间元素；
   若中间元素小于第一个指针，即它位于后面的递增数组，更新第二指针指向中间元素；
   第一指针总是指向前面，第二指针总是指向后面；
   当两指针相邻时，第二指针指向最小元素。
   特殊情况，当第一指针=第二指针=中间元素，可能出现 [1,0,1,1,1]，此时之能从头到尾遍历。
'''

class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if len(numbers) < 1:
            return None
        left = 0
        right = len(numbers) - 1
        while numbers[left] >= numbers[right]:
            if right-left == 1:
                return numbers[right]
            mid = (left+right) // 2
            if numbers[left] == numbers[right] and numbers[right] == numbers[mid]:
                return self.minNum(left, right, numbers)
            if numbers[left] <= numbers[mid]:
                left = mid
            else:
                right = mid
        # 没有旋转
        return numbers[left]


    def minNum(self, left, right, numbers):
        r = numbers[left]
        for i in range(left+1, right+1):
            if r > numbers[i]:
                r = numbers[i]
        return r


if __name__ == '__main__':
    a = Solution()
    print (a.minArray([1,3,5]))













