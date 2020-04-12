# -*- coding:utf-8 -*-
'''
重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

example:
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

解：采用递归。前序遍历第一个数为根节点，记录该数在中序遍历中的位置，前面的是左子树，后面的是右子树。
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
        	return None
        root = TreeNode(preorder[0])
        splitNum = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:splitNum+1], inorder[:splitNum])
        root.right = self.buildTree(preorder[splitNum+1:], inorder[splitNum+1:])
        return root


if __name__ == '__main__':
	a = Solution()
	root = a.buildTree([3,9,20,15,7], [9,3,15,20,7])
	print (root.val)
	print (root.left.val)
	print (root.right.val)
	print (root.right.left.val)
	print (root.right.right.val)
