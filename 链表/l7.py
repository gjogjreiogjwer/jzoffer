# -*- coding:utf-8 -*-
# 链表中环的入口结点
# 一个链表中包含环，请找出该链表的环的入口结点。
# 解：首先需要知道环中有几个结点，采用快慢指针：一个每次走两步，一个每次走一步。
#    当快慢指针相遇，说明存在环，并且两个指针是在环中相遇。
#    然后从该节点前进并计数，当再次回到这个节点时，就得到环中节点数。
#    已知环中节点数n，设置两个指针，一个指针先往前移动n位，之后两指针一起移动。
#    当两个指针相遇时，即指向入口节点，

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None:
        	return None
        node = self.hasLoop(pHead)
        if node == None:
            return None
        count = 1
        node_copy = node
        node = node.next
        while node != node_copy:
            node = node.next
            count += 1
        p1 = pHead
        p2 = pHead
        for i in range(count):
            p1 = p1.next
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    def hasLoop(self, pHead):
        p1 = pHead.next
        if p1 == None:
            return None
        p2 = p1.next
        while p1 != None and p2 != None:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
            if p2 != None:
                p2 = p2.next
        return None

if __name__ == '__main__':
    q = ListNode(1)
    w = ListNode(2)
    e = ListNode(3)
    r = ListNode(4)
    t = ListNode(5)
    y = ListNode(6)
    q.next = w
    w.next = e
    e.next = r
    r.next = t
    t.next = y
    y.next = e
    b = Solution()
    res = b.EntryNodeOfLoop(q)
    print (res.val)
























