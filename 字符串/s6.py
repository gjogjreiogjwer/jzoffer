# -*- coding:utf-8 -*-
# 把字符串转换成整数
# 将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 
# 数值为0或者字符串不是一个合法的数值则返回0。
# 输入描述：
# 输入一个字符串,包括数字字母符号,可以为空
# 输出描述：
# 如果是合法的数值表达则返回该数字，否则返回0
# 解：首先判断有无正负符号，再用ord()返回字符的ASCII码。

class Solution:
    def StrToInt(self, s):
        # write code here
        flag = False
        passive = 1
        if len(s) <= 0:
        	return 0
        if s[0] == '+':
        	flag = True
        elif s[0] == '-':
        	flag = True
        	passive = -1
        begin = 0
        if flag == True:
        	begin = 1
        num = 0
        for i in s[begin:]:
        	if i <= '9' and i >= '0':
        		num = num*10+(ord(i)-ord('0'))*passive
        	else:
        		return 0
        return num

if __name__ == '__main__':
    b=Solution()
    print (b.StrToInt('-123'))