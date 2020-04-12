# -*- coding:utf-8 -*-
'''
n个骰子的点数
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

example1:
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]

example2:
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]


解：动态规划
n个骰子，每个骰子6个面，总情况数为6^n
设F(n,s)为当骰子数为n，和为s的情况数量。
当n=1时，F(1,s)=1,其中s=1,2,3,4,5,6
当n≥2时，F(n,s)=F(n−1,s−1)+F(n−1,s−2)+F(n−1,s−3)+F(n−1,s−4)+F(n−1,s−5)+F(n−1,s−6)
'''

class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        import numpy as np
        array = np.zeros((n+1, n*6+1))
        for k in range(1,7):
            array[1][k] = 1
        for i in range(2, n+1):
            for j in range(i, 6*i+1):
                for k in range(1,7):
                    # j-k需要在n-1中存在
                    if j-k < i-1:
                        break
                    array[i][j] += array[i-1][j-k]
        total = pow(6, n)
        res = array[n] / total
        return res[n:]

if __name__ == '__main__':
    a = Solution()
    print (a.twoSum(1))





















