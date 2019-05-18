# -*- coding:utf-8 -*-
# 反转链表
# 输入一个链表，反转链表后，输出链表的所有元素。
# 解：设置两个指针temp和cur，替换得到1-->none, 2-->1,3-->2....

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
        	return pHead
        cur=None
        while pHead:
        	temp=pHead
        	pHead=pHead.next
        	temp.next=cur
        	cur=temp
        return cur

if __name__ == '__main__':
    q=ListNode(1)
    w=ListNode(2)
    e=ListNode(3)
    q.next=w
    w.next=e
    b=Solution()
    print b.ReverseList(q).next.next.val
