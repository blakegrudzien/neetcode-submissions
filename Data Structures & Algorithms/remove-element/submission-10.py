class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        total = 0
        l = 0
        r = len(nums)-1

        while l <= r:
            if nums[l] == val:

                while nums[r] == val:
                    print(nums[r])
                    print(r)
                    print(nums)
                    
                    r-=1
                    if r <= 0 or r< l:
                        return total
                nums[l] = nums[r]
                r-=1
                total+=1
            else:
                total+=1  
            l+=1
        return total
                
                

        
                

                
        