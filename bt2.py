# -*- coding:utf-8 -*-
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
	def inorder(self, pRootOfTree):
		if not pRootOfTree:
			return []
		return self.inorder(pRootOfTree.left)+[pRootOfTree]+self.inorder(pRootOfTree.right)


	def Convert(self, pRootOfTree):
		res=self.inorder(pRootOfTree)
		if len(res)<=1: 
			return pRootOfTree
		res[0].left=None
		res[0].right=res[1]
		res[-1].right=None
		res[-1].left=res[-2]
		for i in range(1,len(res)-1):
			res[i].left=res[i-1]
			res[i].right=res[i+1]
		return res[0]



if __name__ == '__main__':
	q=TreeNode(5)
	w=TreeNode(3)
	e=TreeNode(7)
	r=TreeNode(2)
	t=TreeNode(4)
	y=TreeNode(6)
	u=TreeNode(8)

	q.left=w
	q.right=e
	w.left=r
	w.right=t
	e.left=y
	e.right=u
	b=Solution()
	print b.Convert(q).val
