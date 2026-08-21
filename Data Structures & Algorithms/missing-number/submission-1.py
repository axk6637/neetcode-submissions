class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #[0,2]


        res=len(nums)

        for i in range(len(nums)): #2 0,1
            res+= (i- nums[i]) #0-0 =0 1-2=1 

        return res


