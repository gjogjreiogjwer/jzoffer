# -*- coding:utf-8 -*-
# 第一个只出现一次的字符
# 在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置。
# 解：采用字典。

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        count = {}
        c = 0
        for i in s:
            count[i] = count.get(i, 0)+1
        for i in s:
            if count[i] == 1:
                return c
            else:
                c += 1
        if c == len(s):
            return -1

if __name__ == '__main__':
    b = Solution()
    print (b.FirstNotRepeatingChar("hufaehufe"))