# -*- coding:utf-8 -*-
'''
表示数值的字符串
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、
"3.1416"、"0123"及"-1E-16"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

解：使用正则。
   首先可能有正负号，若干个0-9的整数部分（有些小数没有整数部分）
   如果是小数，有小数点，后接若干0-9
   如果用科学技术法，e或E，后接一个整数，可能有正负号。
   e前面必须有数
'''

import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = re.compile(r'^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$')
        return bool(p.match(s.strip()))

if __name__ == '__main__':
    b=Solution()
    print (b.isNumber('2.'))