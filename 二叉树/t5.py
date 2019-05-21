# -*- coding:utf-8 -*-
# 二叉树中和为某一值的路径
# 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
# 解：采用深度优先搜索。当为叶子节点且与给定数值相减为0，即为该路径满足条件。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
     # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        if not root.left and not root.right and expectNumber == root.val:
            return [[root.val]]
        result = []
        left = self.FindPath(root.left, expectNumber-root.val)
        right = self.FindPath(root.right, expectNumber-root.val)
        # i是列表，left + right: [[  ], [  ]]
        for i in left+right:
            result.append([root.val]+i)
        return result

if __name__ == '__main__':
    q = TreeNode(1)
    w = TreeNode(2)
    e = TreeNode(3)
    r = TreeNode(4)
    t = TreeNode(5)
    y = TreeNode(4)
    q.left = w
    q.right = e
    w.left = r
    w.right = t
    b = Solution()
    print (b.FindPath(q,8))









