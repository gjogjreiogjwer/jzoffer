# -*- coding:utf-8 -*-
# 用两个栈实现队列
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
# 解：用列表实现。

class Solution:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def push(self, node):
		# write code here
		self.stack1.append(node)

	def pop(self):
		# return xx
		if not self.stack2:
			while self.stack1:
				self.stack2.append(self.stack1.pop())
		return self.stack2.pop()


if __name__ == '__main__':
	b = Solution()
	b.push(1)
	b.push(2)
	#b.pop()
	print (b.stack1)
