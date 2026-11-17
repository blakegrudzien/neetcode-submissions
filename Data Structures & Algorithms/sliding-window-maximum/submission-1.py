class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = []

        r = 0
        l = 0
        res = []
        while r<len(nums):
            
            while stack and stack[-1] < nums[r]:
                stack.pop()
            stack.append(nums[r])

            if r>=k-1:

                res.append(stack[0])
                if nums[l] == stack[0]:
                    stack.pop(0)
                l+=1
                
            r+=1
        return res
         

            
        