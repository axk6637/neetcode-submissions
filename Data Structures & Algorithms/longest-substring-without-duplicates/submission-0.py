class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        res=0
        l=0
        for r in range(len(s)):
            while s[r] in charSet:#sliding window 
                charSet.remove(s[l]) #shrink window until no duplicate
                l+=1
            charSet.add(s[r]) 
            res= max(res, r-l+1)
        return res