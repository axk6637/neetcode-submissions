class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        #1011 res+=1 #101 %2=1 #10 %2=0 #1%2=1 
        while n:
            res+= n%2
            n=n >>1

        return res