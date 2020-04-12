# -*- coding:utf-8 -*-
'''
二叉树的深度
输入一棵二叉树的根节点，求该树的深度。
从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

example:
给定二叉树 [3,9,20,null,null,15,7]，
返回它的最大深度 3 

解： 采用深度优先搜索。每一次返回时+1.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


if __name__ == '__main__':
    a = Solution()
    q = TreeNode(3)
    w = TreeNode(9)
    e = TreeNode(20)
    r = TreeNode(15)
    t = TreeNode(7)
    q.left = w
    q.right = e
    e.left = r
    e.right = t
    print (a.maxDepth(q))