class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        amount = 0
        key = {0:1}
        count = 0


        for i, v in enumerate(nums):
            amount+= v
            if amount-k in key:
                count+= key[amount-k]
            key[amount] = key.get(amount,0) + 1
        return count


            
        