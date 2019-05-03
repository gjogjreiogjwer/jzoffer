# -*- coding:utf-8 -*-
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
        if not root.left and not root.right and expectNumber==root.val:
            print [[root.val]]
            return [[root.val]]
        result=[]
        left=self.FindPath(root.left,expectNumber-root.val)
        right=self.FindPath(root.right,expectNumber-root.val)
        for i in left+right:
            print 'i',i
            result.append([root.val]+i)
            print 'r',result
        return result


if __name__ == '__main__':
    q=TreeNode(1)
    w=TreeNode(2)
    e=TreeNode(3)
    r=TreeNode(4)
    t=TreeNode(5)
    y=TreeNode(4)
    q.left=w
    q.right=e
    w.left=r
    w.right=t
    # e.left=y
    b=Solution()
    print b.FindPath(q,8)









