# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.result=[]

    def Permutation(self, ss):
        # write code here
        if len(ss)<=0:
            return []
        self.perm(ss,0)
        sorted(self.result)
        return self.result

    def perm(self,ss,begin):
        if begin==len(ss):
            self.result.append(ss)
            return 
        for i in range(begin,len(ss)):
            if i!=begin and ss[i]==ss[begin]:
                continue
            str1=list(ss)
            str1[i],str1[begin]=str1[begin],str1[i]
            ss=''.join(str1)
            self.perm(ss,begin+1)


if __name__ == '__main__':
	q=Solution()
	print q.Permutation('abc')
