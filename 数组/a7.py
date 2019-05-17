# -*- coding:utf-8 -*-
class Solution:
    count=0

    def InversePairs(self, data):
        # write code here
        sortData=self.mergesort(data)
        return self.count%1000000007

    def mergesort(self,data):
        if len(data)<=1:
            return data
        middle=len(data)/2
        left=self.mergesort(data[:middle])
        right=self.mergesort(data[middle:])
        return self.merge(left,right)

    def merge(self,left,right):
        global count
        l1=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                l1.append(left[i])
                i+=1
            else:
                l1.append(right[j])
                j+=1
                self.count+=len(left)-i
        if i==len(left):
            l1.extend(right[j:])
        else:
            l1.extend(left[i:])
        return l1


if __name__ == '__main__':
    b=Solution()
    a=[1,2,3,4,0]
    print b.InversePairs(a)


















        			