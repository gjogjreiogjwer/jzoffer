# -*- coding:utf-8 -*-
# 从尾到头打印链表
# 输入一个链表，返回一个反序的链表。
# 解：把链表的值插入到列表的首位

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        while listNode:
            res.insert(0, listNode.val)
            listNode = listNode.next
        return res

if __name__ == '__main__':
    q = ListNode(1)
    w = ListNode(2)
    e = ListNode(3)
    q.next = w
    w.next = e
    b = Solution()
    print (b.printListFromTailToHead(q))




