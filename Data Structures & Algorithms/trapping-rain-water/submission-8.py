class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        water = 0
        while height[l] == 0:
            l+=1
            if l == len(height):
                return 0
        
        while l<len(height):
            temp = l+1
            r = l+1

            while temp< len(height) and height[temp]<height[l]:
                if height[temp] > height[r]:
                    r = temp
                temp+=1
            if temp != len(height):
                r = temp
            if r == len(height) or height[r] == 0:
                return water
            h = min(height[l],height[r])
            l+=1
            while l<r:
                water+=(h-height[l])
                l+=1
        return water 

        