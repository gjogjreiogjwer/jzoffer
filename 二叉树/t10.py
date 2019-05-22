# -*- coding:utf-8 -*-
# 按之字顺序打印二叉树
# 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
# 第三行按照从左到右的顺序打印，其他行以此类推。
# 解：采用队列。使用两个列表，一排信息存在temp中，当遍历到一排的最后一个节点时，按要求正序或逆序把temp存入res，清空temp。
#    用队列的时候，把根节点存入列表 [pRoot]
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self, pRoot):
        # write code here    
        if not pRoot:
            return []
        res = []
        flag = True
        q = [pRoot]
        temp = []
        last = pRoot
        while len(q):
            t = q.pop(0)
            temp.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
            if t == last:
                if flag:
                    res.extend(temp)
                else:
                    res.extend(temp[::-1])
                flag = not flag
                temp = []
                if len(q):
                    last = q[-1]
        return res

if __name__ == '__main__':
    q = TreeNode(8)
    w = TreeNode(6)
    e = TreeNode(10)
    r = TreeNode(5)
    t = TreeNode(7)
    y = TreeNode(9)
    u = TreeNode(11)
    q.left = w
    q.right = e
    w.left = r
    w.right = t
    e.left = y
    e.right = u
    b = Solution()
    print (b.Print(q))










            
