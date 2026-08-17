class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1
        m = 0
        temp = 0

        while l < r:
            temp = (min(heights[l],heights[r])) * (r-l)
            
            if temp > m:
                m = temp
                
            temp = 0
            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        return m 
             