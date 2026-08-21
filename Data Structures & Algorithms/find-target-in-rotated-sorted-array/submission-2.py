class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r= len(nums)-1
        
        #4,5,6,7,0,1,2 target=7, 2
        #5,6,0,1,2,3,4 target= 2

        while l<=r:
            m=(l+r)//2
            if target==nums[m]:
                return m
            if nums[l]<=nums[m]:
                if nums[m]<target or target<nums[l]:
                    l=m+1
                else:
                    r=m-1
            else:
                if target<nums[m] or target> nums[r]:
                    r=m-1
                else:
                    l=m+1


        return -1
        
        