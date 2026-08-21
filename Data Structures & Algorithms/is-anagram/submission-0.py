class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        countS, countT= {}, {} #create 2 hashMaps

        for i in range (len(s)):
            countS[s[i]]= 1 + countS.get(s[i], 0) #will give 0 if the char is not in the hashMap
            countT[t[i]]=1 + countT.get(t[i], 0)
        return countS==countT
