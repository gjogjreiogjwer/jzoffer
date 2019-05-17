# -*- coding:utf-8 -*-
# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
# 例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
# 解：四个变量表示上下左右

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        rows=len(matrix)
        cols=len(matrix[0])
        left=0
        right=cols-1
        up=0
        down=rows-1
        res=[]
        while left<=right and up<=down:
        	for i in range(left,right+1):
        		res.append(matrix[up][i])
        	for i in range(up+1,down+1):
        		res.append(matrix[i][right])
        	if up!=down:
        		for i in range(right-1,left-1,-1):
        			res.append(matrix[down][i])
        	if left!=right:
        		for i in range(down-1,up,-1):
        			res.append(matrix[i][left])
        	left+=1
        	right-=1
        	up+=1
        	down-=1
        return res

if __name__ == '__main__':
	b=Solution()
	m=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	print b.printMatrix(m)


