# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s==" ":
        	return " "
        r=[]
        ss=s.split(' ')
        for i in range(len(ss)):
        	r.append(ss.pop())
        return ' '.join(r)

if __name__ == '__main__':
	q=Solution()
	print q.ReverseSentence('abcdefr')