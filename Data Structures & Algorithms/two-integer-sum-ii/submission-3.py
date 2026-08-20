class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        
        while l < r:
            curr_total = numbers[l] + numbers[r]
            if curr_total == target:
                return [l+1, r+1]
            if curr_total < target:
                l+=1
               
            else:
                r-=1
            
        return 
                

        