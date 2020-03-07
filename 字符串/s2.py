# -*- coding:utf-8 -*-
# 字符串的排列
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc，
# 则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
# 解：采用递归。
#    首先固定第一个字符，后面所有字符全排列。后面的字符也分为第一个固定，后面全排列。

class Solution:
    def __init__(self):
        self.result = []

    def Permutation(self, ss):
        # write code here
        if len(ss) <= 0:
            return []
        self.perm(ss, 0)
        sorted(self.result)
        return self.result

    def perm(self, ss, begin):
        if begin == len(ss):
            self.result.append(ss)
            return 
        for i in range(begin, len(ss)):
            #如果字符串相同，不交换
            if i != begin and ss[i] == ss[begin]:
                continue
            str1 = list(ss)
            str1[i], str1[begin] = str1[begin], str1[i]
            ss = ''.join(str1)
            self.perm(ss, begin+1)


if __name__ == '__main__':
	b = Solution()
	print (b.Permutation('abc'))
