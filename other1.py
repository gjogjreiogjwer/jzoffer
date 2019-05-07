# -*- coding:utf-8 -*-
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# 解：一个数减去1后与上它本身，会把这个数最右边的1变0.

class Solution:
    def NumberOf1(self, n):
        # write code here
        if n<0:
        	n=n&0xffffffff
        count=0
        while n:
        	count+=1
        	n=n&(n-1)
        return count



# 第二种方法
    def NumberOf2(self, n):
    	return sum([(n>>i)&1 for i in range(32)])


if __name__ == '__main__':
	b=Solution()
	print b.NumberOf2(7)