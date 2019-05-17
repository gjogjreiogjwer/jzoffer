# -*- coding:utf-8 -*-
# 链表中倒数第k个结点
# 输入一个链表，输出该链表中倒数第k个结点。
# 解：设置两个指针指向链表的头，第一个指针向前走（k-1），之后一二两个指针一起
#    向前走，当第一个指针指向链表末尾时，第二个指针指向倒数第k个数。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
    	if not head or k<=0:
    		return None
    	p1=head
    	p2=head
    	for i in range(k-1):
    		if not p1.next:
    			return None
    		else:
    			p1=p1.next
    	while p1.next:
    		p2=p2.next
    		p1=p1.next
    	return p2

	# 使用列表开辟了新空间
 #    def FindKthToTail(self, head, k):
 #        # write code here
 #        list=[]
 #        while head:
 #            list.append(head)
 #            head=head.next
 #        length=len(list)
 #        if k>length or k<1:
 #            return None
 #        return list[-k]

if __name__ == '__main__':
    q=ListNode(1)
    w=ListNode(2)
    e=ListNode(3)
    q.next=w
    w.next=e
    b=Solution()
    print b.FindKthToTail(q, 3).val

    
