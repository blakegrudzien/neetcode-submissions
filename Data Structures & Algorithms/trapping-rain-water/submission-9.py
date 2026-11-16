class Solution:
    def trap(self, height: List[int]) -> int:

        left_tallest = [0] * len(height)
        right_tallest = [0] * len(height)
        water = 0
        i = 1
        while i< len(height):
            if height[i-1] > left_tallest[i-1]:
                left_tallest[i] = height[i-1]
            else:
                left_tallest[i] = left_tallest[i-1]
            if height[len(height)-i] > right_tallest[len(height)-i]:
                right_tallest[len(height)-i-1] = height[len(height)-i]
            else:
                right_tallest[len(height)-i-1] = right_tallest[len(height)-i]
            i+=1
        for i, val in enumerate(height):
            water+= max(min(left_tallest[i],right_tallest[i])- height[i],0)

        return water

             

        
        