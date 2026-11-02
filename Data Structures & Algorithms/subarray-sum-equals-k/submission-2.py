class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * (len(nums)+1)
        count = 0
        key = {}
        prefix[0] = 0

        res = 0
        
        for i, v in enumerate(nums):
            count+=v
            prefix[i+1] = count
            key[count] = key.get(count,0)+1

  
        for i, p in enumerate(prefix):
            if i != 0:
                key[p] -=1
            if p + k in key:
                res+=key[p+k]
 
        return res
        
        
        