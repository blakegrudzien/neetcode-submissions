class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        best = 0
        for i, n in enumerate(nums):
            if i<2:
                dp[i] = nums[i]
            elif i == 2:
                dp[i] = nums[i] + dp[0]
            else:
                dp[i] = nums[i] + max(dp[i-2],dp[i-3])
            best = max(best, dp[i])
        return best

                
        