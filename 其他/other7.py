# -*- coding:utf-8 -*-
# 和为S的连续正数序列
# 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,
# 他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,
# 他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
# 解：两个指针，分别指向序列头尾,不断扩大和缩小两个指针。

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        left = 1
        right = 2
        while left < right:
        	seqSum = (left+right)*(right-left+1)/2
        	if seqSum < tsum:
        		right += 1
        	elif seqSum > tsum:
        		left += 1
        	else:
        		temp = []
        		for i in range(left, right+1):
        			temp.append(i)
        		res.append(temp)
        		left += 1
        return res

if __name__ == '__main__':
	b = Solution()
	print (b.FindContinuousSequence(100))