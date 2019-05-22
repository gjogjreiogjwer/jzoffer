# -*- coding:utf-8 -*-
# 把数组排成最小的数
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# 例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
# 解：重写sorted中key，用cmp_to_key代替cmp，比较str(x)+str(y)和str(y)+str(x)的大小。

class Solution:
	from functools import cmp_to_key

	def PrintMinNumber(self, numbers):
        # write code here
		if len(numbers) == 0:
			return ''
		compare = lambda x, y : (str(x)+str(y) > str(y)+str(x)) - (str(x)+str(y) < str(y)+str(x))
		minString = sorted(numbers, key = self.cmp_to_key(compare))
		return ''.join([str(s) for s in minString])

if __name__ == '__main__':
	b = Solution()
	print (b.PrintMinNumber([3,32,321]))



        