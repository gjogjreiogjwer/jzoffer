# -*- coding:utf-8 -*-
'''
股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

example1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

example2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

解：记录每次的最小价格和最大利润	
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
        	return 0
        profit = 0
        mixPrice = prices[0]
        for i in range(1, n):
        	if prices[i] < mixPrice:
        		mixPrice = prices[i]
        	if prices[i] - mixPrice > profit:
        		profit = prices[i] - mixPrice
        return profit


if __name__ == '__main__':
	a = Solution()
	print (a.maxProfit([10,20,100,1,20]))
        	
        










        			