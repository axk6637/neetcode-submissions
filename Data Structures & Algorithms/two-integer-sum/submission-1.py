class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        U-understand
        I-Input -> array of integers: nums
        O-Output -> indices i and j 
        C=Constraints ->     2 <= nums.length <= 1000
                            -10,000,000 <= nums[i] <= 10,000,000
                            -10,000,000 <= target <= 10,000,000
                            Return the answer with the smaller index first.              
        E-Edge Cases
        - Empty array -> return None
    
        M-Match
        - 

        P-Plan
        1. Intialize a hashmap: hashMap
        2. Loop through the array
        3. calculate the difference which is target- 
        """
        hashMap={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n]=i
        