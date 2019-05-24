# -*- coding:utf-8 -*-
# 数据流中的中位数
# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
# 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
# 我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
# 解：Insert（）进行输入和排序；GetMedian（）取中位数

class Solution:
    def __init__(self):
        self.data = []
        
    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()

    def GetMedian(self):
        # write code here
        n = len(self.data)
        if n%2 == 0:
        	mid = n//2
        	return (self.data[mid]+self.data[mid-1])/2
        else:
        	mid = n//2
        	return self.data[mid]

if __name__ == '__main__':
	b = Solution()
	b.Insert(2)
	b.Insert(4)
	b.Insert(1)
	b.Insert(7)
	print (b.GetMedian())
