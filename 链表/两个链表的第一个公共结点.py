# -*- coding:utf-8 -*-
'''
两个链表的第一个公共结点
输入两个链表，找出它们的第一个公共结点。
解：两个链表如果有重复的节点,则从第一个重复节点之后就都相同了

1. 合并两个链表，一个pHead1在前pHead2在后，一个pHead2在前pHead1在后，同时遍历这两张表，即可得到公共节点。

2. 剪掉长链表的头，同时遍历两个长度相等的链表
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 解法1
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        p1, p2 = pHead1, pHead2
        while p1 != p2:
            p1 = p1.next if p1 != None else pHead2
            p2 = p2.next if p2 != None else pHead1
        return p1

    # 解法2
    def FindFirstCommonNode2(self, headA, headB):
        if not headA or not headB:
            return None
        lenA = 1
        lenB = 1
        p1 = headA
        p2 = headB
        while p1.next != None:
            p1 = p1.next
            lenA += 1
        while p2.next != None:
            p2 = p2.next
            lenB += 1
        difference = lenA - lenB
        if difference > 0:
            for i in range(abs(difference)):
                headA = headA.next
            while headA != headB:
                headA = headA.next
                headB = headB.next
        else:
            for i in range(abs(difference)):
                headB = headB.next
            while headA != headB:
                headA = headA.next
                headB = headB.next
        return headA

if __name__ == '__main__':
    q = ListNode(1)
    w = ListNode(2)
    e = ListNode(3)
    a = ListNode(5)
    q.next = w
    w.next = e
    a.next = w
    b = Solution()
    res = b.FindFirstCommonNode(q,a)
    print (res.val)




