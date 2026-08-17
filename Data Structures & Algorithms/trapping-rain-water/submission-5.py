class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) < 3:
            return 0
        key = {}
        total = 0
        l = 0

        while height[l] ==0:
            l+=1
        

        i = height[l]
        for i in range(l):
            if i != 0:
                key[i] = l

        
        while l < len(height):
            if height[l] != 0:
                for j in range(height[l]):
                    if j in key:

                        total += l-(key[j])-1
                    key[j] = l
                    
            l+=1
        return total