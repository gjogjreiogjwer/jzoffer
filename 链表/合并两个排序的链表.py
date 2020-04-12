# -*- coding:utf-8 -*-
'''
合并两个排序的链表
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

example:
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

解：判断两表是否为空，一表为空则返回另外一个表（停止条件）。接下来设置两个指针，
   判断两个表中较小的当前值放入新的链表。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            x = l2
            x.next = self.mergeTwoLists(l1, l2.next)
        else:
            x = l1
            x.next = self.mergeTwoLists(l1.next, l2)
        return x

if __name__ == '__main__':
    q = ListNode(1)
    w = ListNode(3)
    e = ListNode(7)
    a = ListNode(2)
    b = ListNode(9)
    q.next = w
    w.next = e
    a.next = b
    b = Solution()
    print (b.mergeTwoLists(q,a).next.next.val)
