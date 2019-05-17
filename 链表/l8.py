# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead==None or pHead.next==None:
            return pHead
        p=pHead.next
        if pHead.val!=p.val:
            pHead.next=self.deleteDuplication(p)
        else:
            while p.next!=None and p.val==pHead.val:
                p=p.next
            if p.val!=pHead.val:
                pHead=self.deleteDuplication(p)
            else:
                return None
        return pHead


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



if __name__ == '__main__':
    q=ListNode(1)
    w=ListNode(2)
    e=ListNode(3)
    r=ListNode(3)
    t=ListNode(3)
    y=ListNode(4)
    u=ListNode(4)
    i=ListNode(5)
    q.next=w
    w.next=e
    e.next=r
    r.next=t
    t.next=y
    y.next=u
    u.next=i
    b=Solution()
    print b.deleteDuplication(q).next.next.val


























