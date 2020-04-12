# -*- coding:utf-8 -*-
'''
和为S的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

example1:
输入：target = 9
输出：[[2,3,4],[4,5]]

example2:
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]

解：和为s系列：头尾两个指针
两个指针，分别指向序列头尾,不断扩大和缩小两个指针。
'''

class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        left = 1
        right = 2
        while left < right:
            sumArray = (left+right) * (right-left+1) // 2
            if sumArray < target:
                right += 1
            elif sumArray > target:
                left += 1
            else:
                temp = []
                for i in range(left, right+1):
                    temp.append(i)
                res.append(temp)
                left += 1
        return res

if __name__ == '__main__':
    a = Solution()
    print (a.findContinuousSequence(9))
