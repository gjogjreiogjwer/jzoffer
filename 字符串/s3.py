# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        count={}
        c=0
        for i in s:
            count[i]=count.get(i,0)+1
        for i in s:
            if count[i]==1:
                return c
            else:
                c+=1
        if c==len(s):
            return -1