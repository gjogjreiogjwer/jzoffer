# -*- coding:utf-8 -*-
# 二维数组中的查找
# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# 解：取右上角数字，若大于tartget，去掉这一列；若小于target，下移一行。

class Solution:
    def find(self, target, array):
        row = len(array)
        line = len(array[0])
        if row > 0 and line > 0:
            x = 0
            y = line-1
            while x < row and y >= 0:
                if array[x][y] == target:
                    return True
                if array[x][y] < target:
                    x += 1
                else:
                    y -= 1;
        return False

if __name__ == '__main__':
    b = Solution()
    array = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    print (b.find(3,array))