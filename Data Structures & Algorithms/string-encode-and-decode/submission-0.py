class Solution:

    def encode(self, strs: List[str]) -> str:
        #we are going to encode in: lengthostring#string format
        res="" #empty string to store the encoded string

        for s in strs:
            res+=str(len(s)) +"#" +s
        return res

    def decode(self, s: str) -> List[str]:
        res=[]#create an empty list to store decoded strings
        i=0 #intialize the pointer

        while i< len(s):
            j=i
            while s[j]!='#':
                j+=1
            length = int(s[i:j]) #i inclusive j not inclusive 
            i=j+1
            j=i+length 
            res.append(s[i:j])
            i=j
        return res
