class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    backtrack(i+1, curr)
                    curr.pop()
            return

        backtrack(0, [])
        return res
        