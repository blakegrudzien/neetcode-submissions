class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        amount = 0
        key = {0:1}
        total = 0
        for v in nums:
            amount +=v
            if amount-k in key:
                total += key[amount-k]
            key[amount] = key.get(amount,0) +1

        return total

        