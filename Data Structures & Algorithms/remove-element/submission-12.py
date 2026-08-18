class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        l, r, total = 0, len(nums)-1, 0

        while l <= r:
            if nums[l] == val:
                while r>=l and nums[r] == val:
                    r-=1
                if r <= l:
                    return total
                nums[l] = nums[r]
                total+=1
                r-=1
            else:
                total+=1
            l+=1
        return total
        

                

        
                

                
        