# -*- coding:utf-8 -*-
# 机器人的运动范围
# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下
# 四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，
# 机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
# 请问该机器人能够达到多少个格子？
# 解：走过的点用字典做标记。

class Solution:
	def __init__(self):
		self.dic = {}

	def movingCount(self, threshold, rows, cols):
		# write code here
		return self.moving(threshold, rows, cols , 0, 0)

	def moving(self, threshold, rows, cols, i, j):
		if i%10+i//10+j%10+j//10 > threshold:
			return 0
		if i < 0 or j < 0 or i >= rows or j >= cols:
			return 0
		if (i, j) in self.dic:
			return 0
		self.dic[(i, j)]=1
		return 1+self.moving(threshold, rows, cols, i+1, j)+self.moving(threshold, rows, cols, i-1, j)+self.moving(threshold, rows,cols, i, j+1)+self.moving(threshold, rows, cols, i, j-1)

if __name__ == '__main__':
	b = Solution()
	print (b.movingCount(5, 13, 14))