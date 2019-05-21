# -*- coding:utf-8 -*-
# 重建二叉树
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
# 解：采用递归。前序遍历第一个数为根节点，记录该数在中序遍历中的位置，前面的是左子树，后面的是右子树。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            pos = tin.index(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:pos+1], tin[:pos])
            root.right = self.reConstructBinaryTree(pre[pos+1:], tin[pos+1:])
        return root

if __name__ == '__main__':
    q=[1,2,4,7,3,5,6,8]
    w=[4,7,2,1,5,3,8,6]
    b=Solution()
    print (b.reConstructBinaryTree(q,w).val)
    
