# -*- coding:utf-8 -*-
'''
删除链表的节点
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
返回删除后的链表的头节点。

example1:
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

example2:
输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

解：
pre和head指向同一个对象，对pre修改会改变head，但pre和head不同
e.g. 4,5,1,9  1
pre: 5,9
head: 4,5,9
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        if head.val == val:
            return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur:
            pre.next = cur.next
        return head

if __name__ == '__main__':
    a = Solution()
    q = ListNode(4)
    w = ListNode(5)
    e = ListNode(1)
    r = ListNode(9)
    q.next = w
    w.next = e
    e.next = r
    print (a.deleteNode(q, 5))