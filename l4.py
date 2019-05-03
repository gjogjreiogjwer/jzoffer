# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
        	return pHead2
        if not pHead2:
        	return pHead1
        pmerge=None
        if pHead1.val>=pHead2.val:
        	pmerge=pHead2
        	pmerge.next=self.Merge(pHead1,pHead2.next)
        else:
        	pmerge=pHead1
        	pmerge.next=self.Merge(pHead1.next,pHead2)
        return pmerge



class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

if __name__ == '__main__':
    q=ListNode(1)
    print q
    w=ListNode(3)
    e=ListNode(7)
    q.next=w
    w.next=e
    a=ListNode(2)
    b=ListNode(9)
    a.next=b
    b=Solution()
    print b.Merge(q,a).next.next.val
