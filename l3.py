# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
        	return pHead
        cur=None
        while pHead:
        	tmp=pHead
        	pHead=pHead.next
        	tmp.next=cur
        	cur=tmp
        return cur




class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

if __name__ == '__main__':
    q=ListNode(1)
    w=ListNode(2)
    e=ListNode(3)
    q.next=w
    w.next=e
    b=Solution()
    print b.ReverseList(q).next.next.next
