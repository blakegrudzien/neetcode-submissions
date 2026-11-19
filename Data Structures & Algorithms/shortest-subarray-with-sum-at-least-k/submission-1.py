class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        curr_min = len(nums)+1
        pre = [0] * (len(nums)+1)
        p = nums[0]
        pre[0] = 0
        
        for i,v in enumerate(nums):
            pre[i+1] = pre[i]+v
        stack = []
        for r in range(len(pre)):
            while stack and pre[r]-pre[stack[0]] >= k:
                curr_min = min(curr_min,r-stack[0])
                stack.pop(0)
            while stack and pre[r] < pre[stack[-1]]:
                stack.pop()
            stack.append(r)
        if curr_min == len(nums)+1:
            return -1
        return curr_min
            
                

            

        

