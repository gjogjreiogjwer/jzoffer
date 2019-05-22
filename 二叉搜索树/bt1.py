# -*- coding:utf-8 -*-
# 二叉搜索树的后序遍历序列
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
# 解：采用递归。首先判断左右子树的范围，再判断它们是不是符合二叉树标准。
#    然后对左右子树进行递归。

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not len(sequence):
        	return False
        if len(sequence) == 1:
        	return True
        root = sequence[-1]
        i = 0
        while sequence[i] < root:
        	i += 1
        for j in range(i, len(sequence)-1):
        	if sequence[j] < root:
        		return False
        left = sequence[:i]
        right = sequence[i:len(sequence)-1]
        l, r = True, True
        if len(left) > 0:
	       	l = self.VerifySquenceOfBST(left)
        if len(right) > 0:
       		r = self.VerifySquenceOfBST(right)
       	return l and r

if __name__ == '__main__':
	b = Solution()
	print (b.VerifySquenceOfBST([1,3,2,6,5,4]))