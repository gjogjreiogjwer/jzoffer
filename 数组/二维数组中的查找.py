# -*- coding:utf-8 -*-
'''
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

解：取右上角数字，若大于target，去掉这一列；若小于target，下移一行。
'''

class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        x = 0
        y = len(matrix[0]) - 1
        while x < len(matrix) and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False

if __name__ == '__main__':
    a = Solution()
    array = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    print (a.findNumberIn2DArray(array, 9))
