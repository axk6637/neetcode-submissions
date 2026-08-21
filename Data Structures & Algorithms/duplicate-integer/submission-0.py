class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #use hashset as it stores unique values, good for lookup
         Hash_set= set()
         for i in nums:
            if i in Hash_set:
                return True
            Hash_set.add(i)
         return False 
            