class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums) #convert list to set for O(1) lookup

        longest=0 #tracker for longest sequence
        for num in numSet:
            if (num-1) not in numSet: #start of sequence -> is there a num less than me?
                length=1 #if not, count me as sequence of length 1 
                while (num+length) in numSet: #is there a number bigger than me consecutively?
                    length+=1 #if yes, increment seq len
                longest= max(length, longest) #of all seq which is max?

        return longest #return final
                