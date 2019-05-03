
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        n=len(rotateArray)
        if n<=1:
            return rotateArray
        left=0
        right=n-1
        while rotateArray[left]>=rotateArray[right]:
            if (right-left)==1:
                mid=right
                break
            mid=(left+right)/2
            if rotateArray[left]==rotateArray[mid] and rotateArray[right]==rotateArray[mid]:
                return self.minNum(left,right,rotateArray)
            if(rotateArray[mid]>=rotateArray[left]):
                left=mid
            else:
                right=mid
        return rotateArray[mid]


    def minNum(self,left,right,rotateArray):
        r=rotateArray[left]
        for i in range(left+1,right+1):
            if r>rotateArray[i]:
                r=rotateArray[i]
        return r












