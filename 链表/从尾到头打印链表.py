# -*- coding:utf-8 -*-
'''
从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

example:
输入：head = [1,3,2]
输出：[2,3,1]

解：把链表的值插入到列表的首位
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        reverseArray = []
        while head:
            reverseArray.insert(0, head.val)
            head = head.next
        return reverseArray


if __name__ == '__main__':
    a = Solution()
    q = ListNode(1)
    w = ListNode(3)
    e = ListNode(2)
    q.next = w
    w.next = e
    print (a.reversePrint(q))
