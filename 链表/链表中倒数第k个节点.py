# -*- coding:utf-8 -*-
'''
链表中倒数第k个结点
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

example:
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.

解：设置两个指针指向链表的头，第一个指针向前走（k-1），之后一二两个指针一起
   向前走，当第一个指针指向链表末尾时，第二个指针指向倒数第k个数。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        p1 = head
        p2 = head
        for i in range(k-1):
            if not p2:
                return None
            p2 = p2.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        return p1


if __name__ == '__main__':
    q = ListNode(1)
    w = ListNode(2)
    e = ListNode(3)
    q.next = w
    w.next = e
    b = Solution()
    print (b.getKthFromEnd(q, 3).val)


    
