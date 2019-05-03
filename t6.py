# -*- coding:utf-8 -*-
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
        left=self.TreeDepth(pRoot.left)
        right=self.TreeDepth(pRoot.right)
        return max(left,right)+1


if __name__ == '__main__':
    q=TreeNode(1)
    w=TreeNode(2)
    e=TreeNode(3)
    r=TreeNode(4)
    q.left=w
    q.right=e
    w.left=r
    b=Solution()
    print b.TreeDepth(q)