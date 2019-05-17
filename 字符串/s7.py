# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        i=0
        j=0
        if len(s)==0 and len(pattern)==0:
            return True
        elif len(s)==0 and len(pattern)!=0:
            if pattern[-1]=='*':
                return True
            else:
                return False
        elif len(s)!=0 and len(pattern)==0:
            return False
        while i<len(s) and j<len(pattern):
            if s[i]==pattern[j] or pattern[j]=='.':
                i+=1
                j+=1
                continue
            elif j<len(pattern)-1:
                if s[i]!=pattern[j] and pattern[j]!='*':
                    return False
                elif s[i]!=pattern[j] and pattern[j]=='*':
                    j+=2
                    continue
            elif j==len(pattern)-1:
                if pattern[j]=='*':
                    return True
            else:
                return False
        if i==len(s) and j==len(pattern):
            return True
        elif i==len(s) and j<len(pattern):
            if pattern[-1]=='*':
                return True
            else: 
                return False
        elif i<len(s) and j==len(pattern):
            while i<j-1:
                if s[i]==pattern[j-3]:
                    i+=1
            if s[i]==pattern[j-1]:
                return True
            else:
                return False











