class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        m = 0
        temp = 0

        while r < len(prices):
            temp = prices[r]-prices[l]

            if temp > m:
                m =temp
            temp = 0

            if prices[l] >prices[r]:
                l = r 
            r+=1
        return m
        