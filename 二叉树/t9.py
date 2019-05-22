# -*- coding:utf-8 -*-
# 对称的二叉树
# 请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
# 解：判断true/false采用递归。判断每一个左右子树是否对称相等。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here 
        if not pRoot:
            return True
        if pRoot.left and not pRoot.right:
            return False
        if not pRoot.left and pRoot.right:
            return False
        return self.isSame(pRoot.left,pRoot.right) 

    def isSame(self, p1, p2):
            if not p1 and not p2:
                return True
            elif (p1 and p2) and p1.val == p2.val:
                return isSame(p1.left, p2.right) and isSame(p1.right, p2.left)
            else: 
                return False
        
if __name__ == '__main__':
    q = TreeNode(8)
    w = TreeNode(6)
    e = TreeNode(9)
    r = TreeNode(5)
    t = TreeNode(7)
    y = TreeNode(7)
    u = TreeNode(5)
    q.left = w
    q.right = e
    w.left = r
    w.right = t
    e.left = y
    e.right = u
    b = Solution()
    print (b.isSymmetrical(q))
    










