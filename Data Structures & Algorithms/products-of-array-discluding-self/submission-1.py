class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = nums.copy()
        curr_prod = 1
        answer[0] = 1
        for i in range(1,len(nums)):
            answer[i] = nums[i-1] * curr_prod
            curr_prod = answer[i]
        print(answer)
        curr_prod = 1
        for i in range(1,len(nums)+1):
            
            answer[len(nums)-i] = answer[len(nums)-i] * curr_prod
            curr_prod = nums[len(nums)-i] * curr_prod
        return answer

        