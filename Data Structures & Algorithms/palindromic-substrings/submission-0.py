class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        

        for i in range(len(s)):

            #for odd length palindromes:
            l=i
            r=i
            res+= self.helper(s, l, r)
            #for even length pal:
            res+= self.helper(s, l, r+1)
        return res

    def helper(self, s, l, r):
        res=0
        while l>=0 and r<len(s) and s[l]==s[r]:
                    l-=1
                    r+=1
                    res+=1
        return res