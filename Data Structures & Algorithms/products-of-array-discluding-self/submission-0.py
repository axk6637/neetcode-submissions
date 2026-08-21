class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1] *(len(nums)) #create a list with [1,1,1,1] if it's [1,2,3,4]

        prefix=1 #set default prefix=1
        for i in range (len(nums)):
            res[i] =prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1, -1, -1):
            res[i]*=postfix
            postfix*=nums[i]
        return res

        #Time complexity: O(n)
        #Space complaxity: O(n) for res and O(1) for scalar variables: prefix, postfix