# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        minK=self.findMin(data,k,0,len(data)-1)
        maxK=self.findMax(data,k,0,len(data)-1)
        if minK==-1:
            return 0
        return maxK-minK+1



    def findMin(self,data,k,lo,hi):
        if lo>hi:
            return -1
        mid=lo+(hi-lo)/2
        if data[mid]==k:
            if mid==lo:
                return mid
            if data[mid-1]!=k:
                return mid
            else:
                return self.findMin(data,k,lo,mid-1)
        if data[mid]>k:
            return self.findMin(data,k,lo,mid-1)
        else:
            return self.findMin(data,k,mid+1,hi)

    def findMax(self,data,k,lo,hi):
        if lo>hi:
            return -1
        mid=lo+(hi-lo)/2
        if data[mid]==k:
            if mid==hi:
                return mid
            if data[mid+1]!=k:
                return mid
            else:
                return self.findMax(data,k,mid+1,hi)
        if data[mid]>k:
            return self.findMax(data,k,lo,mid-1)
        else:
            return self.findMax(data,k,mid+1,hi)










