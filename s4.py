# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if len(s)<=0:
            return ''
        s_list=list(s)
        for i in range(n):
            s_list.append(s_list.pop(0))
        return ''.join(s_list)

if __name__=='__main__':
	q=Solution()
	print q.LeftRotateString('asdfg',2)
