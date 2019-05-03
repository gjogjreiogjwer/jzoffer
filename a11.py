# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        b=[]
        if len(A)==0:
            return b
        for i in range(len(A)):
            temp=A[i]
            A[i]=1
            b.append(reduce(lambda x,y:*y,A))
            A[i]=temp
        return b