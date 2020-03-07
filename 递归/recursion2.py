# -*- coding:utf-8 -*-
# 跳台阶
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法
#（先后次序不同算不同的结果）。
# 解：1,2,3,5...裴波那契数列。

class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 1:
        	return number
        first = 1
        second = 1
        for i in range(2, number+1):
        	res = first+second
        	first = second
        	second = res
        return res

if __name__ == '__main__':
	b = Solution()
	print (b.jumpFloor(5))