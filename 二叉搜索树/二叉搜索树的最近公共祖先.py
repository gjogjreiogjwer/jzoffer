# -*- coding:utf-8 -*-
'''
二叉搜索树的最近公共祖先
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大
（一个节点也可以是它自己的祖先）。”

example1:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。

example2:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

解：判断p，q是否都在root的同一边
if p，q都小于root, root = root.left
if p，q都大于root, root = root.right
if p，q在root的两边，root就是最近公共祖先节点
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
        	return None
        if p.val < root.val and q.val < root.val:
        	return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
        	return self.lowestCommonAncestor(root.right, p, q)
        else:
        	return root

if __name__ == '__main__':
	a = Solution()
	root = TreeNode(6)
	q = TreeNode(2)
	w = TreeNode(8)
	e = TreeNode(0)
	r = TreeNode(4)
	t = TreeNode(7)
	y = TreeNode(9)
	u = TreeNode(3)
	i = TreeNode(5)
	root.left = q
	root.right = w
	q.left = e
	q.right = r
	w.left = t
	w.right = y
	r.left = u
	r.right = i
	print (a.lowestCommonAncestor(root, q, w))
