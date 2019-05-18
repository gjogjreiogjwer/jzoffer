# -*- coding:utf-8 -*-
# 合并两个排序的链表
# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
# 解：判断两表是否为空，一表为空则返回另外一个表（停止条件）。接下来设置两个指针，
#    判断两个表中较小的当前值放入新的链表。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
        	return pHead2
        if not pHead2:
        	return pHead1
        pmerge=None
        if pHead1.val>=pHead2.val:
        	pmerge=pHead2
        	pmerge.next=self.Merge(pHead1,pHead2.next)
        else:
        	pmerge=pHead1
        	pmerge.next=self.Merge(pHead1.next,pHead2)
        return pmerge


if __name__ == '__main__':
    q=ListNode(1)
    w=ListNode(3)
    e=ListNode(7)
    a=ListNode(2)
    b=ListNode(9)
    q.next=w
    w.next=e
    a.next=b
    b=Solution()
    print b.Merge(q,a).next.next.val
