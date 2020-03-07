# -*- coding:utf-8 -*-
# 序列化二叉树
# 请实现两个函数，分别用来序列化和反序列化二叉树
# 解：$表示none，用逗号隔开。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.flag = -1

    def Serialize(self, root):
        s = ""
        s = self.recursion(root, s)
        return s

    def recursion(self, root, s):
    	if not root:
    		return '$,'
    	s = str(root.val)+','
    	left = self.recursion(root.left, s)
    	right = self.recursion(root.right, s)
    	s += left+right
    	return s

    def Deserialize(self, s):
        # write code here
        self.flag += 1
        root = None
        l = s.split(',')
        if self.flag >= len(s):
        	return None
        if l[self.flag] != '$':
        	root = TreeNode(int(l[self.flag]))
        	root.left = self.Deserialize(s)
        	root.right = self.Deserialize(s)
        return root

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
    print (b.Serialize(q))
    print (b.Deserialize('8,6,5,$,$,7,$,$,10,9,$,$,11,$,$,').val)