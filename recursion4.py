# -*- coding:utf-8 -*-
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
class Solution:
    def rectCover(self, number):
        # write code here
        if number<=2:
        	return number
        first=1
        second=2
        for i in range(3,number+1):
        	res=first+second
        	first=second
        	second=res
        return res

if __name__ == '__main__':
	b=Solution()
	print b.rectCover(5)