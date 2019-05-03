# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead==None:
        	return None
        node=self.hasLoop(pHead)
        if node==None:
            return None
        count=1
        node_copy=node
        node=node.next
        while node!=node_copy:
            node=node.next
            count+=1
        p1=pHead
        p2=pHead
        for i in range(count):
            p1=p1.next
        while p1!=p2:
            p1=p1.next
            p2=p2.next
        return p1

    def hasLoop(self,pHead):
        p1=pHead.next
        if p1==None:
            return None
        p2=p1.next
        while p1!=None and p2!=None:
            if p1==p2:
                return p1
            p1=p1.next
            p2=p2.next
            if p2!=None:
                p2=p2.next
        return None
        





class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    q=ListNode(1)
    w=ListNode(2)
    e=ListNode(3)
    r=ListNode(4)
    t=ListNode(5)
    y=ListNode(6)
    q.next=w
    w.next=e
    e.next=r
    r.next=t
    t.next=y
    y.next=e
    b=Solution()
    print b.EntryNodeOfLoop(q).val
























