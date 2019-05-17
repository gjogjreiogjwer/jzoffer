# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return pHead
        p=RandomListNode(pHead.label)
        p.random=pHead.random
        p.next=self.Clone(pHead.next)
        return p



class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

if __name__ == '__main__':
    q=RandomListNode(1)
    w=RandomListNode(2)
    e=RandomListNode(3)
    r=RandomListNode(4)
    q.next=w
    w.next=e
    e.next=r
    q.random=e
    w.random=r
    b=Solution()
    n=b.Clone(q)
    print n.next
    
