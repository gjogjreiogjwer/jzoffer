# -*- coding:utf-8 -*-
'''
替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

example:
输入：s = "We are happy."
输出："We%20are%20happy."

解：使用replace函数。
'''

class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.replace(' ', '%20')

    # 解2：正则
    def replaceSpace1(self, s):
    	import re
    	return re.sub(' ', '%20', s)

if __name__ == '__main__':
	a = Solution()
	print (a.replaceSpace1('we are happy'))