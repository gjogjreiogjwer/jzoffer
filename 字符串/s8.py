# -*- coding:utf-8 -*-
import re
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        return re.match(r'^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$',s)

if __name__ == '__main__':
    q=Solution()
    print q.isNumeric('+100')