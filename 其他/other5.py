# -*- coding:utf-8 -*-
# 求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
# 为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
# ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
# 解：对个位来说：若个位大于0，出现次数cur*1+1；若个位等于0，出现次数cur*1
# 对其他位：每一位的权值base（10，100...），该位的值weight，该位之前的数former
# 若weight=0，1出现次数cur*base；若weight=1，出现次数cur*base+former+1；若weight》1，出现次数cur*base+base

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        base=1
        count=0
        cur=n
        while cur:
        	weight=cur%10
        	cur/=10
        	count+=base*cur
        	if weight==1:
        		count+=n%base+1
        	elif weight>1:
        		count+=base
        	base*=10
        return count

if __name__ == '__main__':
	b=Solution()
	print b.NumberOf1Between1AndN_Solution(534)