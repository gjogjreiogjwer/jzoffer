# -*- coding:utf-8 -*-
# 构建乘积数组
# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
# 其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
# 解：使用reduce累加函数。

class Solution:
    from functools import reduce

    def multiply(self, A):
        # write code here
        b = []
        if len(A) == 0:
            return b
        for i in range(len(A)):
            temp = A[i]
            A[i] = 1
            b.append(self.reduce(lambda x, y : x*y, A))
            A[i] = temp
        return b

if __name__ == '__main__':
    b = Solution()
    print (b.multiply([2,3,4,5]))