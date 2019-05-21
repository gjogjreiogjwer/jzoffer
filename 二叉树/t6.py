# -*- coding:utf-8 -*-
# 二叉树的深度
# 输入一棵二叉树，求该树的深度。
# 从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
# 解： 采用深度优先搜索。每一次返回时+1.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left, right)+1

if __name__ == '__main__':
    q = TreeNode(1)
    w = TreeNode(2)
    e = TreeNode(3)
    r = TreeNode(4)
    q.left = w
    q.right = e
    w.left = r
    b = Solution()
    print (b.TreeDepth(q))