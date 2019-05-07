# -*- coding:utf-8 -*-
# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
# 解：递归

class Solution:
    def Sum_Solution(self, n):
        # write code here
        if n==0:
        	return 0
        return n+self.Sum_Solution(n-1)

if __name__ == '__main__':
	b=Solution()
	print b.Sum_Solution(3)