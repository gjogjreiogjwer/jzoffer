# -*- coding:utf-8 -*-
# 平衡二叉树
# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
# 解：返回true/false的题目一般采用递归。
#    平衡二叉树左右子树高度差不超过1.
#    计算每个节点左右子树的深度差。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        if abs(self.treeDepth(pRoot.left)-self.treeDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def treeDepth(self,pRoot):
        if not pRoot:
            return 0
        left = self.treeDepth(pRoot.left)
        right = self.treeDepth(pRoot.right)
        return max(left, right)+1

if __name__ == '__main__':
    q = TreeNode(1)
    w = TreeNode(2)
    e = TreeNode(3)
    r = TreeNode(4)
    t = TreeNode(5)
    y = TreeNode(6)
    q.left = w
    q.right = e
    w.left = r
    w.right = t
    e.left = y
    b = Solution()
    print (b.IsBalanced_Solution(q))









