# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        list1=[]
        list2=[]
        while listNode:
            list1.append(listNode.val)
            listNode=listNode.next
        while len(list1)!=0:
            list2.append(list1.pop())
        return list2

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

if __name__ == '__main__':
    q=ListNode(1)
    w=ListNode(2)
    e=ListNode(3)
    q.next=w
    w.next=e
    b=Solution()
    print b.printListFromTailToHead(q)




