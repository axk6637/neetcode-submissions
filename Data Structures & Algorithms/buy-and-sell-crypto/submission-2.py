class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointer approach:
        l=0
        r=1
        maxp=0

        while r<len(prices):
            if prices[l]<prices[r]:
                p=prices[r]-prices[l]
                maxp=max(maxp,p)
            else:
                l=r
            r+=1
        return maxp

        """
       #Greedy:
        min_price= float('inf') #min price
        max_profit=0 #find max profit

        for price in prices: #go through each price once
            if price<min_price:
                min_price=price
            else:
                profit= price-min_price

                if profit> max_profit:
                    max_profit=price

        return max_profit


        min= float('inf')
        max=0

        for p in prices:
            if p<min:
                min=p
            else:
                profit= p-min
            
                if profit>max:
                    max=profit
        return max        
        """