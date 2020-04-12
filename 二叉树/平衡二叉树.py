# -*- coding:utf-8 -*-
'''
平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

example1:
给定二叉树 [3,9,20,null,null,15,7]
返回 true 。

example2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
返回 false 。

解：返回true/false的题目一般采用递归。
   平衡二叉树左右子树高度差不超过1.
   计算每个节点左右子树的深度差。
'''

class TreeNode(object):
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

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


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
    print (a.isBalanced(q))









