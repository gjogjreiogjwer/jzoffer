# -*- coding:utf-8 -*-
# 数组中只出现一次的数字
# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。
# 请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
# 解：采用字典

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        l1=[]
        count={}
        for i in array:
            count[i] = count.get(i,0)+1
        for i in count.keys():
            if count[i] == 1:
                l1.append(i)
        return l1

if __name__ == '__main__':
    b = Solution()
    print (b.FindNumsAppearOnce([2,3,4,4,6,6,3,1]))