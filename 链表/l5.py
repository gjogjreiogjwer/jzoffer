# -*- coding:utf-8 -*-
# 复杂链表的复制
# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
# 返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
# 解：创建一个新的节点，分别处理label,next和random。

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return pHead
        p=RandomListNode(pHead.label)
        p.random=pHead.random
        p.next=self.Clone(pHead.next)
        return p

if __name__ == '__main__':
    q=RandomListNode(1)
    w=RandomListNode(2)
    e=RandomListNode(3)
    r=RandomListNode(4)
    q.next=w
    w.next=e
    e.next=r
    q.random=e
    w.random=r
    b=Solution()
    res=b.Clone(q)
    print res.label
    print res.next.label
    
