class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #using bucket sort algorithm
        count={} #hashMap to store the frequency of each num

        freq= [[] for i in range (len(nums)+1)] #creatinng bucket/array freq where i is the frequency of number and freq[i] would be the num itself
                                                #len(nums)+1 because the max frequency will be the size of input itself plus 1 for index alignment ie. frequency=index
        for num in nums: #go through each number in the input list
            count[num]= 1 +count.get(num,0) #count the number of frequency of each number
        for num, cnt in count.items(): #go through each key-value pair in count
            freq[cnt].append(num) #add it to the bucket according to the count/index

        res=[] #empty list
        for i in range (len(freq)-1,0,-1): #so if len(freq)=6 then range(5,0,-1) go descending cause we need most frequent

            for num in freq[i]: #go through each num in that bucket
                res.append(num) #add each num to result
                if len(res)==k: #check if the length of the res is equal to k
                    return res  #if true, return it/ bound to be a result so no retun statement outside for loop