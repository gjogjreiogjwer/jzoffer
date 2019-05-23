# -*- coding:utf-8 -*-
# 替换空格
# 请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.
# 则经过替换之后的字符串为We%20Are%20Happy。
# 解：使用replace函数。

class Solution:
	def replaceSpace(self, s):
	    return s.replace(" ", "%20")

if __name__ == '__main__':
	b = Solution()
	print (b.replaceSpace("we are happy."))