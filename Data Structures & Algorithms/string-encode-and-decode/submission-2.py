class Solution:

    def encode(self, strs: List[str]) -> str:
        #we are going to encode in: lengthostring#string format
        res="" #empty string to store the encoded string
        #["Hello","World"]
        for s in strs:
            res+=str(len(s)) +"#" +s
        return res

    def decode(self, s: str) -> List[str]:
        res=[]#create an empty list to store decoded strings
        i=0 #intialize the pointer

        # "5#hello5#world"
        # i<14
        #j=0, j=1
        #length= 5, i=2, j=2+5, res=2-7, i=7
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
"""

        #encode
        res=""
        for s in strs:
            res+= str(len(s))+"#"+s
        
        return res
        #  5#hello5#world
        res=[]
        i=0
        while i<len(s):
            j=i #0
            while s[j]!="#":
                j+=1 #1
            length=int(s[i:j]) #5
            i=j+1 #2
            j=i+length #7
            res.append(s[i:j])
            i=j
        return res
"""

