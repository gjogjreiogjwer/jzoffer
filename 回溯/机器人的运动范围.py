# -*- coding:utf-8 -*-
'''
机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，
因为3+5+3+8=19。请问该机器人能够到达多少个格子？

example1:
输入：m = 2, n = 3, k = 1
输出：3

example2:
输入：m = 3, n = 1, k = 0
输出：1

解：走过的点用字典做标记。
'''

class Solution(object):

	def __init__(self):
		self.list = []

	def movingCount(self, m, n, k):
	    """
	    :type m: int
	    :type n: int
	    :type k: int
	    :rtype: int
	    """
	    self.m = m
	    self.n = n
	    self.k = k
	    return self.moving(0, 0)


	def moving(self, x, y):
		if x < 0 or y < 0 or x >= self.m or y >= self.n:
			return 0
		if self.sum0(x, y) > self.k:
			return 0
		if (x, y) in self.list:
			return 0
		self.list.append((x,y))
		return 1 + self.moving(x+1, y) + self.moving(x-1, y) + self.moving(x, y+1) + self.moving(x, y-1)

	def sum0(self, x, y):
		s = 0
		for k in (x, y):
			while k:
				s += k % 10
				k //= 10
		return s


if __name__ == '__main__':
	a = Solution()
	print (a.movingCount(3,1,0))