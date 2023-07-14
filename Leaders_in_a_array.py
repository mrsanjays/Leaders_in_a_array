"""
Given an integer array A containing N distinct integers, you have to find all the leaders in array A. An element is a leader if it is strictly greater than all the elements to its right side.

PS: The rightmost element is always a leader.
"""
class Solution:
    @staticmethod
    def reverse(array):
        i,j=0,len(array)-1
        while i<j:
            array[i],array[j]=array[j],array[i]
            i+=1
            j-=1
        return array
    @staticmethod
    def Leaders_in_a_array(array):
        n=len(array)
        res=[]
        max=float('-inf')
        for i in range(n-1,-1,-1):
            if array[i]>max:
                max=array[i]
                res.append(max)
        return Solution().reverse(res)


if __name__ == '__main__':
    ob=Solution()
    array=list(map(int,input().split()))
    print(*ob.Leaders_in_a_array(array))