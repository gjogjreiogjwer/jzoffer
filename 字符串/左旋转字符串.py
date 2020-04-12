# -*- coding:utf-8 -*-
'''
左旋转字符串
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，
该函数将返回左旋转两位得到的结果"cdefgab"。

解：把字符串转化为列表。
'''

class Solution:
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        left = s[:n]
        right = s[n:]
        res = []
        res.append(right)
        res.append(left)
        return ''.join(res)

    def reverseLeftWords1(self, s, n):
        # write code here
        if len(s) <= 0:
            return ''
        s_list = list(s)
        for i in range(n):
            s_list.append(s_list.pop(0))
        return ''.join(s_list)

if __name__=='__main__':
	b = Solution()
	print (b.reverseLeftWords('asdfg', 2))
