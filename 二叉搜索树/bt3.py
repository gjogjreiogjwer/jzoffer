# -*- coding:utf-8 -*-
# 二叉搜索树的第k个结点
# 给定一棵二叉搜索树，请找出其中的第k小的结点。例如，（5，3，7，2，4，6，8）中，
# 按结点数值大小顺序第三小结点的值为4。
# 解：二叉搜索树的中序遍历即时排序的顺序。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        res = self.inorder(pRoot)
        if k <= 0 or k > len(res):
        	return None
        return res[k-1]

    def inorder(self, pRoot):
    	if not pRoot:
    		return []
    	return self.inorder(pRoot.left)+[pRoot]+self.inorder(pRoot.right)

if __name__ == '__main__':
	q = TreeNode(5)
	w = TreeNode(3)
	e = TreeNode(7)
	r = TreeNode(2)
	t = TreeNode(4)
	y = TreeNode(6)
	u = TreeNode(8)
	q.left = w
	q.right = e
	w.left = r
	w.right = t
	e.left = y
	e.right = u
	b = Solution()
	print (b.KthNode(q,3).val)
