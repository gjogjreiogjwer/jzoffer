# -*- coding:utf-8 -*-
# 二叉树的镜像
# 操作给定的二叉树，将其变换为源二叉树的镜像。
# 解：对每一个节点的左右节点进行交换。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here    
        if not root:
            return None
        root.left, root.right = root.right, root.left
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
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
	print (b.Mirror(q).right.right.val)











