# -*- coding:utf-8 -*-
# 和为S的两个数字
# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
# 解：两个指针分别遍历一边数组，两个字典一个记录乘积一个记录对应位置的左边指针。

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        n = len(array)
        temp = {}
        res = {}
        k = 0
        for i in range(n):
        	for j in range(i+1, n):
        		if array[i]+array[j] == tsum:
        			res[k] = array[i]*array[j]
        			temp[k] = i
        			k += 1
        			continue
        if not res:
        	return []
        result = sorted(res.items(), key=lambda x:x[1])
        s1 = array[temp[result[0][0]]]
        s2 = result[0][1]//s1
        return s1, s2

if __name__ == '__main__':
	b = Solution()
	array = [1,2,4,7,11,15]
	print (b.FindNumbersWithSum(array, 15))
