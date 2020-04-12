# -*- coding:utf-8 -*-
'''
把字符串转换成整数

写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。
首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
在任何情况下，若函数不能进行有效的转换时，请返回 0。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−pow(2,31),  pow(2,31) − 1]。
如果数值超过这个范围，请返回  pow(2,31) − 1 或 −pow(2,31)

example1:
输入: "42"
输出: 42

example2:
输入: "   -42"
输出: -42

example3:
输入: "4193 with words"
输出: 4193

example4:
输入: "words and 987"
输出: 0

解：首先判断有无正负符号，再用ord()返回字符的ASCII码。
'''

class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        sign = 1
        num = 0
        if not str:
            return 0
        if str[0] == '+':
            sign = 1
            str = str[1:]
        elif str[0] == '-':
            sign = -1
            str = str[1:]
        for word in str:
            if word > '9' or word < '0':
                break
            else:
                num = 10*num + (ord(word)-ord('0'))*sign
        if num > pow(2, 31) - 1:
            return pow(2, 31) - 1
        elif num < -pow(2, 31):
            return -pow(2, 31)
        return num

if __name__ == '__main__':
    a = Solution()
    print (a.strToInt("      -11919730356x"))

