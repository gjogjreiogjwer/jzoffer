# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        flag=False
        passive=1
        if len(s)<=0:
        	return 0
        if s[0]=='+':
        	flag=True
        elif s[0]=='-':
        	flag=True
        	passive=-1
        begin=0
        if flag==True:
        	begin=1
        num=0
        for i in s[begin:]:
        	if i<='9' and i>='0':
        		num=num*10+(ord(i)-ord('0'))*passive
        	else:
        		return 0
        return num

if __name__ == '__main__':
    q=Solution()
    print q.StrToInt('123')