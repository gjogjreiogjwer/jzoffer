# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        p1,p2=pHead1,pHead2
        while p1!=p2:
            if p1!=None:
                p1=p1.next
            else:
                p1=pHead2
            p2=p2.next if p2!=None else pHead1
        return p1

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    q=ListNode(1)
    w=ListNode(2)
    e=ListNode(3)
    q.next=w
    w.next=e
    a=ListNode(5)
    s=ListNode(6)
    a.next=w
    b=Solution()
    print b.FindFirstCommonNode(q,a)




