class Solution:
    def findMin(self, nums: List[int]) -> int:
        #[1,2,3,4,5]
        #[3,4,5,1,2] 
        #mid=5 check 5<2, l=m+1= 1(3)
        #3<4, m= 3+(4-3)/2=3 , 1<2 yes, r=m=3 

        l=0
        r= len(nums)-1

        while l<r:
            m=l+(r-l)//2
            if nums[m]< nums[r]:
                r=m
            else:
                l=m+1
        return nums[l]
