# -*- coding:utf-8 -*-
'''
二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大
（一个节点也可以是它自己的祖先）。”

example1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

example2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

解：递归
若root中只包含p则返回p
若root中只包含q则返回q
若root中不包含p也不包含q则返回NULL
若root中同时包含p和q，则返回root（此时root为最近公共祖先）

解法2: DFS
记录到p，q的路径，第一个不同点的前面那个就是最近公共祖先节点
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
        if not root or root == p or root == q:
        	return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 不在左边
        if not left:
        	return right
        # 不在右边
        if not right:
        	return left
        # 一个在左，一个在右
        return root


    def lowestCommonAncestor1(self, root, p, q):
    	list1 = []
    	list2 = []
    	self.DFS(root, p, list1)
    	self.DFS(root, q, list2)
    	for i in range(min(len(list1), len(list2))):
    		if list1[i] == list2[i]:
    			continue
    		return list1[i-1]

    def DFS(self, root, node, stack):
    	if not root:
    		return False
    	stack.append(root)
    	if node.val == root.val:
    		return True
    	if self.DFS(root.left, node, stack) or self.DFS(root.right, node, stack):
    		return True
    	stack.pop()
    	return False



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
	print (a.lowestCommonAncestor1(root, q, w))
