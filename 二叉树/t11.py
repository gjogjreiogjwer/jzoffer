# -*- coding:utf-8 -*-
# 把二叉树打印成多行
# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
# 解：采用列表，用队列的时候，把根节点存入列表 [pRoot]。思路和t10相同。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
        	return []
        temp = [pRoot]
        res = []
        t = []
        last = pRoot
        while len(temp):
        	cur = temp.pop(0)
        	t.append(cur.val)
        	if cur.left:
        		temp.append(cur.left)
        	if cur.right:
        		temp.append(cur.right)
        	if cur == last:
        		res.append(t)
        		t = []
        		if len(temp):
        			last = temp[-1]
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
    b=  Solution()
    print (b.Print(q))











            
