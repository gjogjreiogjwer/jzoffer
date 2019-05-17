# -*- coding:utf-8 -*-
# 请实现一个函数用来找出字符流中第一个只出现一次的字符。
# 例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
# 当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
# 如果当前字符流没有存在出现一次的字符，返回#字符。

class Solution:
	# 返回对应char
	def __init__(self):
		self.s=''
		self.res={}

	def FirstAppearingOnce(self):
		# write code here
		length=len(self.s)
		for i in range(length):
			if self.res[self.s[i]]==1:
				return self.s[i]
		return '#'

	def Insert(self, char):
		# write code here
		self.s+=char
		self.res[char]=self.res.get(char,0)+1

if __name__ == '__main__':
	b=Solution()
	b.Insert('g')
	b.Insert('o')
	b.Insert('o')
	b.Insert('g')
	b.Insert('l')
	b.Insert('e')
	print b.FirstAppearingOnce()



