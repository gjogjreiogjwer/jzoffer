# -*- coding:utf-8 -*-
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
            tmp=pNode.right
            while tmp.left:
                tmp=tmp.left
            return tmp
        else:
            while pNode.next:
                if pNode==pNode.next.left:
                    return pNode.next
                pNode=pNode.next
            return None


if __name__ == '__main__':
    q=TreeLinkNode(1)
    w=TreeLinkNode(2)
    e=TreeLinkNode(3)
    r=TreeLinkNode(4)
    q.left=w
    q.right=e
    e.right=r
    w.next=q
    e.next=q
    r.next=e
    b=Solution()
    print b.GetNext(r)
