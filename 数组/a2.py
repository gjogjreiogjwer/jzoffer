# -*- coding:utf-8 -*-
# 旋转数组的最小数字
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，
# 输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
# 解：采用二分法。设置两个指针，分别指向头尾。
#    若中间元素大于第一个指针，即它位于前面的递增数组，更新第一指针指向中间元素；
#    若中间元素小于第一个指针，即它位于后面的递增数组，更新第二指针指向中间元素；
#    第一指针总是指向前面，第二指针总是指向后面；
#    当两指针相邻时，第二指针指向最小元素。
#    特殊情况，当第一指针=第二指针=中间元素，可能出现 [1,0,1,1,1]，此时之能从头到尾遍历。

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        n = len(rotateArray)
        if n <= 1:
            return rotateArray
        left = 0
        right = n-1
        while rotateArray[left] >= rotateArray[right]:
            if (right-left) == 1:
                mid = right
                break
            mid = (left+right)//2
            if rotateArray[left] == rotateArray[mid] and rotateArray[right] == rotateArray[mid]:
                return self.minNum(left,right, rotateArray)
            if(rotateArray[mid] >= rotateArray[left]):
                left = mid
            else:
                right = mid
        return rotateArray[mid]

    def minNum(self, left, right, rotateArray):
        r = rotateArray[left]
        for i in range(left+1, right+1):
            if r > rotateArray[i]:
                r = rotateArray[i]
        return r

if __name__ == '__main__':
    b = Solution()
    print (b.minNumberInRotateArray([3,4,5,1,2]))












