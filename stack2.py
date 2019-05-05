# -*- coding:utf-8 -*-
# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
class Solution:
	def __init__(self):
		self.stack1=[]
		self.stack2=[]

	def push(self, node):
		# write code here
		self.stack1.append(node)
		if not self.stack2:
			self.stack2.append(node)
		if node<self.stack2[-1]:
			self.stack2.append(node)

	def pop(self):
		# write code here
		if self.stack2[-1]==self.stack1[-1]:
			self.stack2.pop()
		self.stack1.pop()

	def top(self):
		# write code here
		return self.stack1[-1]

	def min(self):
		# write code here
		return self.stack2[-1]