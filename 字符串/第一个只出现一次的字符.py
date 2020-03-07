# -*- coding:utf-8 -*-
'''
第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。
解：采用字典。
'''

class Solution:
    def FirstNotRepeatingChar(self, s):
        if len(s) < 1:
            return " "
        dict = {}
        for char in s:
            dict[char] = dict.get(char, 0) + 1
        for char in s:
            if dict[char] == 1:
                return char
        return " "

if __name__ == '__main__':
    b = Solution()
    print (b.FirstNotRepeatingChar("hufaehufe"))