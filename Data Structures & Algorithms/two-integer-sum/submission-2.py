class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}

        for i, v in enumerate(nums):
            if v in ans:
                return [ans[v],i]
            else:
                ans[target-v] = i
        
        