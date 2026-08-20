class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        curr_key = set()
        for i, val in enumerate(nums):
            curr_key.clear()
            p = i+1
            
            while p< len(nums):
                if nums[p] in curr_key:
                    new_match = [val, (nums[p]+val) * -1, nums[p]]
                    if new_match not in ans:
                        ans.append(new_match)
                
                curr_key.add((nums[p]+val) * -1)
                p+=1
        return ans 
                    


            


        