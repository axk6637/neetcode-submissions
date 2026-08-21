class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums) #[-1]

        curMax=1
        curMin=1

        for num in nums:
            if num==0:
                curMin,CurMax=1,1

            maxnum= num*curMax
            curMax=max(num*curMax, num*curMin, num) #[-1,-1,2]
            curMin=min(maxnum, num*curMin, num)

            res=max(res, curMax)

        return res