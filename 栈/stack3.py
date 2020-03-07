# -*- coding:utf-8 -*-
# 栈的压入、弹出序列
# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的
# 一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
# 解；遍历pushV，每一次比较加入s的值是否是popV的第一个值（即出栈），是的话pop并while比较

class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) != len(popV):
        	return False
        s = []
        for i in pushV:
        	s.append(i)
        	while len(s) and s[-1] == popV[0]:
        		s.pop()
        		popV.pop(0)
        if popV:
        	return False
        return True

if __name__ == '__main__':
	b = Solution()
	print (b.IsPopOrder([1,2,3,4,5], [4,5,3,2,1]))