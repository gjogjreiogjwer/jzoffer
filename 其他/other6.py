# -*- coding:utf-8 -*-
# 丑数
# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
# 解：每一个丑数都是前面的丑树乘以2，3，5得到的。

class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 7:
        	return index
        res = [1, 2, 3, 4, 5, 6]
        t1, t2, t3 = 1, 2, 3
        for i in range(6, index):
        	res.append(min(res[t1]*5, min(res[t2]*3, res[t3]*2)))
        	while res[t1]*5 <= res[i]:
        		t1 += 1
        	while res[t2]*3 <= res[i]:
        		t2 += 1
        	while res[t3]*2 <= res[i]:
        		t3 += 1
        return res[index-1]

if __name__ == '__main__':
	b = Solution()
	print (b.GetUglyNumber_Solution(10))
