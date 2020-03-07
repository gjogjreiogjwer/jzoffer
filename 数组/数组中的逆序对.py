# -*- coding:utf-8 -*-
'''
数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。
解：采用归并排序。
'''

class Solution(object):
    def __init__(self):
        self.count = 0

    def mergeSort(self, dataset):
        if len(dataset) <= 1:
            return dataset
        mid = len(dataset) // 2
        left = self.mergeSort(dataset[:mid])
        right = self.mergeSort(dataset[mid:])
        # 注意要有return，返回给left，right
        return self.merge(left, right)


    def merge(self, left, right):
        list = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list.append(left[i])
                i += 1
            else:
                list.append(right[j])
                j += 1
                # 重点
                self.count += len(left) - i
        if i == len(left):
            list.extend(right[j:])
        else:
            list.extend(left[i:])
        # 同理return
        return list


    def reversePairs(self, nums):
        self.mergeSort(nums)
        return self.count


if __name__ == '__main__':
    a = Solution()
    print (a.reversePairs([7,5,6,4]))


















        			