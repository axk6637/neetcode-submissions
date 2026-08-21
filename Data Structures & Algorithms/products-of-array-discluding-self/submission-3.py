class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1] *(len(nums)) #create a list with [1,1,1,1] if it's [1,2,3,4]

        prefix=1 #set default prefix=1
        for i in range (len(nums)): #0->4
            res[i] =prefix #[1, 1, 2, 6]
            # [1,2,3,4]
            prefix*=nums[i] #1*1=1, 1*2=2, 2*3=6, (24)
        postfix=1
        for i in range(len(nums)-1, -1, -1):
            res[i]*=postfix #[24,12,8,6] #1,2,3,4
            postfix*=nums[i] #1*4= 4 4*3=12 12*2=24
        return res

        #Time complexity: O(n)
        #Space complaxity: O(n) for res and O(1) extra space for scalar variables: prefix, postfix
        """
        res=[1]* (len(nums))
        prefix=1
        #1,2,3,4
        for i in range (len(nums)):
            res[i]*=prefix 
            prefix*=nums[i] 

        postfix=1
        for i in range(len(nums)-1, -1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        
        return res
        """