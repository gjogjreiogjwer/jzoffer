# -*- coding:utf-8 -*-
'''
构建乘积数组
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

example:
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]

解：对称遍历
B[i]是A[i]左边所有元素 * A[i]右边所有用元素
从左到右累乘，保存在数组res中，res[i]表示A[i]左边所有元素乘积
从右到左累乘到res中
'''

class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        left = 1
        res = []
        for i in range(len(a)):
            res.append(left)
            left *= a[i]
        right = 1
        for i in range(len(a)-1, -1, -1):
            res[i] *= right
            right *= a[i]
        return res

if __name__ == '__main__':
    a = Solution()
    print (a.constructArr([1,2,3,4,5]))