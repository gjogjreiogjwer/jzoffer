# -*- coding:utf-8 -*-
# 数组中出现次数超过一半的数字
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
# 超过数组长度的一半，因此输出2。如果不存在则输出0。
# 解：采用字典，dict.get()。

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        sortDict = {}
        for i in numbers:
            sortDict[i] = sortDict.get(i, 0)+1
        for i in numbers:
            if sortDict[i] >= (len(numbers)//2+1):
                return i
        return 0

if __name__ == '__main__':
	b = Solution()
	print (b.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))







