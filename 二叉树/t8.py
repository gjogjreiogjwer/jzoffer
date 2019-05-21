# -*- coding:utf-8 -*-
# 二叉树的下一个结点
# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
# 解：如果这个节点有右子树，下一个节点就是它右子树的最左子节点。
#    如果这个节点是它的父节点的左节点，下一个节点就是它父节点。
#    如果这个节点是它的父节点的右节点，沿着父节点向上遍历，直到到一个节点是它父节点的左子节点。 

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        elif pNode.right:
            tmp = pNode.right
            while tmp.left:
                tmp = tmp.left
            return tmp
        else:
            while pNode.next:
                if pNode == pNode.next.left:
                    return pNode.next
                pNode = pNode.next
            return None

if __name__ == '__main__':
    q = TreeLinkNode(1)
    w = TreeLinkNode(2)
    e = TreeLinkNode(3)
    r = TreeLinkNode(4)
    q.left = w
    q.right = e
    e.right = r
    w.next = q
    e.next = q
    r.next = e
    b = Solution()
    print (b.GetNext(w).val)
