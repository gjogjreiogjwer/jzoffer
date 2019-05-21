# -*- coding:utf-8 -*-
# 树的子结构
# 输入两颗二叉树A，B，判断B是不是A的子结构。（PS：我们约定空树不是任意一个树的子结构）。
# 解：返回true/false的题目一般采用递归。
#    首先在A中找到和B的根节点的值相同的节点，再判断该子节点的结构是否和B的根节点结构相同。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
        	return False
        return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2) or self.isSubTree(pRoot1, pRoot2)

    def isSubTree(self, p1, p2):
    	if not p2:
    		return True
    	if not p1 or p1.val != p2.val:
    		return False
    	return self.isSubTree(p1.left, p2.left) and self.isSubTree(p1.right, p2.right)

if __name__ == '__main__':
	q=TreeNode(1)
	w=TreeNode(2)
	e=TreeNode(3)
	r=TreeNode(4)
	t=TreeNode(5)
	q.left=w
	q.right=e
	w.left=r
	w.right=t
	a=TreeNode(2)
	s=TreeNode(4)
	d=TreeNode(5)
	a.left=s
	a.right=d
	b=Solution()
	print (b.HasSubtree(q,a))














