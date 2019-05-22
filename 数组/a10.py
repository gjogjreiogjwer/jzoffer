# -*- coding:utf-8 -*-
# 数组中重复的数字
# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
# 也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 
# 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
# 解：0（索引值）和2（索引值位置元素）不相等，并且2和以2为索引值的1也不想等，交换2，1，得[1,3,2,0,2,5,3]
#    0（索引值）和1（索引值位置元素）不相等，并且1和以1为索引值的3也不想等，交换1，3，得[3,1,2,0,2,5,3]
#    0（索引值）和3（索引值位置元素）不相等，并且3和以3为索引值的0也不想等，交换3，0，得[0,1,2,3,2,5,3]
#    0（索引值）和0（索引值位置元素）相等，遍历下一个元素
#    该方法只适用于范围0-n-1

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        n = len(numbers)
        if n == 0:
            return False
        for i in range(n):
            if numbers[i] > n-1 or numbers[i] < 0:
                return False
        for i in range(n):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]
        return False

if __name__ == '__main__':
    b = Solution()
    d = [0]
    print (b.duplicate([2,3,1,0,2,5,3], d))
    print (d)

