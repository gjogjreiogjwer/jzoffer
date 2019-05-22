# -*- coding:utf-8 -*-
# 数字在排序数组中出现的次数
# 统计一个数字在排序数组中出现的次数。
# 解：采用二分法。分别找到这个最左边和最右边这个数的位置。
#    当中间元素等于k，如果该位置=lo，即在数组最左边，返回mid；
#    如果该位置的前一个不等于k，返回mid；
#    不然继续二分。 

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        minK = self.findMin(data, k, 0, len(data)-1)
        maxK = self.findMax(data, k, 0, len(data)-1)
        if minK == -1:
            return 0
        return maxK-minK+1

    def findMin(self, data, k, lo, hi):
        if lo > hi:
            return -1
        mid = lo+(hi-lo)//2
        if data[mid] == k:
            if mid == lo:
                return mid
            if data[mid-1] != k:
                return mid
            else:
                return self.findMin(data, k, lo, mid-1)
        if data[mid] > k:
            return self.findMin(data, k, lo, mid-1)
        else:
            return self.findMin(data, k, mid+1, hi)

    def findMax(self, data, k, lo, hi):
        if lo > hi:
            return -1
        mid = lo+(hi-lo)//2
        if data[mid] == k:
            if mid == hi:
                return mid
            if data[mid+1] != k:
                return mid
            else:
                return self.findMax(data, k, mid+1, hi)
        if data[mid] > k:
            return self.findMax(data, k, lo, mid-1)
        else:
            return self.findMax(data, k, mid+1, hi)

if __name__ == '__main__':
    b=Solution()
    print (b.GetNumberOfK([1,2,2,2,3,3,4,6],2))









