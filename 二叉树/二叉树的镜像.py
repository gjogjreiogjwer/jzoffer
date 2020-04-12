# -*- coding:utf-8 -*-
'''
二叉树的镜像
操作给定的二叉树，将其变换为源二叉树的镜像。

example:
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

解：对每一个节点的左右节点进行交换。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root

if __name__ == '__main__':
    q = TreeNode(8)
    w = TreeNode(6)
    e = TreeNode(10)
    a = TreeNode(5)
    q.left = w
    q.right = e
    w.left = a
    b = Solution()
    print (b.mirrorTree(q).right.right.val)










