class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= defaultdict(list) #making a default dictionary that maps keys-> list of strings, returns an empty list if a key doesn't exist

        for s in strs: #loops through each string s in strs
            count= [0]*26 #initilaize an array/list with 26 0s as a-z [0,0,0,....0]
            for c in s: #loops through each char c in s: e,a,t in "eat"
                count [ord(c)-ord('a')] +=1 #take ascii value of char c and subtract ascii value of 'a' to map each char to index and increment
            res[tuple(count)].append(s)  #append the strings with matching count together, using tuple as list can't be used as key in Python
        return res.values() #return the anagrams grouped together