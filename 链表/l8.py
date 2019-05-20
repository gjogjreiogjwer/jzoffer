# -*- coding:utf-8 -*-
# 删除链表中重复的结点
# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
# 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5。
# 解：设置两个指针，一个指向当前节点pHead，一个指向下一个节点p，如果这两节点相同，p指向下一节点
#    直到不同或是末尾。再用递归对pHead更新。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead==None or pHead.next==None:
            return pHead
        p=pHead.next
        if pHead.val!=p.val:
            pHead.next=self.deleteDuplication(p)
        else:
            while p.next!=None and p.val==pHead.val:
                p=p.next
            if p.val!=pHead.val:
                pHead=self.deleteDuplication(p)
            else:
                return None
        return pHead

if __name__ == '__main__':
    q=ListNode(1)
    w=ListNode(2)
    e=ListNode(3)
    r=ListNode(3)
    t=ListNode(3)
    y=ListNode(4)
    u=ListNode(4)
    i=ListNode(5)
    q.next=w
    w.next=e
    e.next=r
    r.next=t
    t.next=y
    y.next=u
    u.next=i
    b=Solution()
    res=b.deleteDuplication(q)
    print res.val
    print res.next.val
    print res.next.next.val
    print res.next.next.next


























