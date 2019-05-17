    class Solution:
        def reOrderArray(self, array):
            n=len(array)
            if n<=1:
                return array
            l=0
            for i in range(n):
                if array[i]%2==1:
                    array.insert(l,array.pop(i))
                    l+=1
            return array


if __name__ == '__main__':
    q=Solution()
    print q.reOrderArray([7,3,2,6,5])











