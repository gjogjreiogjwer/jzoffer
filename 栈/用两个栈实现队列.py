# -*- coding:utf-8 -*-
'''
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

example1:
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

example2:
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

解：用列表实现。
'''

class CQueue(object):

    def __init__(self):
    	self.queue = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)


    def deleteHead(self):
        """
        :rtype: int
        """
        if not self.queue:
        	return -1
        return self.queue.pop(0)

if __name__ == '__main__':
	a = CQueue()
	print (a.deleteHead())
	print (a.appendTail(5))
	print (a.appendTail(2))
	print (a.deleteHead())
	print (a.deleteHead())
