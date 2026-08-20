class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow, fast = 0, 1
        max_profit = 0

        while fast < len(prices):
            max_profit = max(max_profit, prices[fast] - prices[slow])
            if prices[slow] > prices[fast]:
                slow+=1
            else:
                fast +=1
        return max_profit


        