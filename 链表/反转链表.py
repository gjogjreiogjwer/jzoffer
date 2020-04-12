# -*- coding:utf-8 -*-
'''
反转链表
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

example:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

解：设置两个指针temp和cur，替换得到1-->none, 2-->1,3-->2....
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        x = None
        while head:
            later = head.next
            head.next = x
            x = head
            head = later
        return x

if __name__ == '__main__':
    q = ListNode(1)
    w = ListNode(2)
    e = ListNode(3)
    q.next = w
    w.next = e
    b = Solution()
    print (b.reverseList(q).next.next.val)