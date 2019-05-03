# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        l1=[]
        maxOfEvery=[]
        n=len(array)
        whetherHasPositive=False
        if array[0]>0:
        	l1.append(0)
        	whetherHasPositive=True
        for i in range(1,n):
        	if array[i]>0 and array[i-1]<=0:
        		l1.append(i)
        		whetherHasPositive=True
        if not whetherHasPositive: #考虑全负数
        	return max(array)
        for i in l1:
        	maxOfEvery.append(self.FindSumOfEvery(i,array))
        return max(maxOfEvery)




    def FindSumOfEvery(self,i,array):
    	listSum=[]
    	sum=0
    	for l in range(i,len(array)):
    		sum+=array[l]
    		listSum.append(sum)
    	return max(listSum)















