# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers)==0:
        	return ''
        compare=lambda x,y:cmp(str(x)+str(y),str(y)+str(x))
        minString=sorted(numbers,cmp=compare)
        return ''.join([str(s) for s in minString])



        