# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        l1=[]
        count={}
        for i in array:
            count[i]=count.get(i,0)+1
        for i in count.keys():
            if count[i]==1:
                l1.append(i)
        return l1