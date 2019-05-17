# -*- coding:utf-8 -*-
# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
# 解：考虑指数为负

class Solution:
    def Power(self, base, exponent):
    	flag=0
    	res=1
    	if exponent<0:
    		flag=1
    	for i in range(abs(exponent)):
    		res*=base
    	if flag==1:
    		res=1/res
    	return res




if __name__ == '__main__':
	b=Solution()
	print b.Power(3.0,2)