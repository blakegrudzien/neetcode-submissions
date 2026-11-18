class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        curr_best = 0
        for i, h in enumerate(heights):
            insert = i
            while stack and stack[-1][0]>h:
                curr_best = max(curr_best,stack[-1][0]*(i-stack[-1][1]))
                insert = stack[-1][1]
                stack.pop()
            stack.append([h,insert])

        while stack:
            curr_best = max(curr_best,stack[-1][0]*(len(heights)-stack[-1][1]))
            stack.pop()
        return curr_best




        