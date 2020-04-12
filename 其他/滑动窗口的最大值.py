# -*- coding:utf-8 -*-
'''
滑动窗口的最大值
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： 
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， 
{2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

解：双端队列
'''

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        # 双端队列思想，可以在头部和尾部分别进行插入删除
        deque = []
        for i in range(len(nums)):
            # 当当前位值比尾部值大时，删除小的值
            while deque and nums[i] >= nums[deque[-1]]:
                deque.pop()
            # 存索引
            deque.append(i)
            # 删除前面滑出窗口的索引
            while i - deque[0] > k-1:
                deque.pop(0)
            if i >= k-1:
                # 头部永远是最大的
                res.append(nums[deque[0]])
        return res




if __name__ == '__main__':
    a = Solution()
    print (a.maxSlidingWindow([7,2,4], 2))