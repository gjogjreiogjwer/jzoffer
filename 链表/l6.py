# -*- coding:utf-8 -*-
# 两个链表的第一个公共结点
# 输入两个链表，找出它们的第一个公共结点。
# 解：合并两个链表，一个pHead1在前pHead2在后，一个pHead2在前pHead1在后，同时遍历这两张表，即可得到公共节点。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        p1,p2=pHead1,pHead2
        while p1!=p2:
            p1=p1.next if p1 != None else pHead2
            p2=p2.next if p2!=None else pHead1
        return p1

if __name__ == '__main__':
    q=ListNode(1)
    w=ListNode(2)
    e=ListNode(3)
    q.next=w
    w.next=e
    a=ListNode(5)
    a.next=w
    b=Solution()
    res=b.FindFirstCommonNode(q,a)
    print (res.val)




