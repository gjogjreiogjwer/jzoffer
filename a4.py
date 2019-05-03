# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        sortDict={}
        for i in numbers:
            sortDict[i]=sortDict.get(i,0)+1
        for i in numbers:
            if sortDict[i]>=(len(numbers)/2+1):
                return i
        return 0








