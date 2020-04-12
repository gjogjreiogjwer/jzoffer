# -*- coding:utf-8 -*-
'''
正则表达式匹配
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

example1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

example2:
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

example3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

example4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

example5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

动态规划
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        r = [[False for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if j == 0:
                    r[i][j] = (i==0)
                else:
                    if p[j-1] != '*':
                        if i>0 and (p[j-1]==s[i-1] or p[j-1]=='.'):
                            r[i][j] = r[i-1][j-1]
                    else:
                        if j >= 2:
                            r[i][j] |= r[i][j-2]
                        if i>=1 and j>=2 and (p[j-2]==s[i-1] or p[j-2]=='.'):
                            r[i][j] |= r[i-1][j]
        return r[n][m]


if __name__ == '__main__':
        a = Solution()
        print (a.isMatch('mississippi', 'mis*is*ip*.'))    












