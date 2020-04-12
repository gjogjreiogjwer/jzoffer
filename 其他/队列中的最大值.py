# -*- coding:utf-8 -*-
'''
队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，
要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1

example1:
输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]

example2:
输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]

解：
当一个元素进入队列的时候，它前面所有比它小的元素就不会再对答案产生影响。
使用两个队列，一个队列为单调递减，最大值既是队列开头，
另一个队列是实际操作队列
'''

class MaxQueue(object):

    def __init__(self):
        self.decreaseQueue = []
        self.queue = []

    def max_value(self):
        """
        :rtype: int
        """
        if not self.decreaseQueue:
            return -1
        return self.decreaseQueue[0]

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        # 实际队列
        self.queue.append(value)
        # 维持self.decreaseQueue单调递减,比value小的数都删除，求最大值是返回self.decreaseQueue第一位的数
        while self.decreaseQueue and self.decreaseQueue[-1] < value:
            self.decreaseQueue.pop()
        self.decreaseQueue.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if not self.decreaseQueue:
            return -1
        res = self.queue.pop(0)
        if res == self.decreaseQueue[0]:
            self.decreaseQueue.pop(0)
        return res
        



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

if __name__ == '__main__':
    a = MaxQueue()
    a.push_back(1)
    a.push_back(2)
    print (a.max_value())
    print (a.pop_front())
    print (a.max_value())







