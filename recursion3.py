# -*- coding:utf-8 -*-
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number<=1:
        	return number
        return pow(2,number-1)

if __name__ == '__main__':
	b=Solution()
	print b.jumpFloorII(5)