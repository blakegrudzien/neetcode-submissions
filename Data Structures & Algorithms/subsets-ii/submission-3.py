class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        prev_list = []
        c = []
        start = 0
        prev_start = 0
        for i in range(len(nums)):
            curr_list = []
            if i == 0 or nums[i] != nums[i-1]:
                ans = ans+prev_list
                for a in ans:
                    c = a.copy()
                    c.append(nums[i])  
                    curr_list.append(c) 
                prev_list = curr_list.copy() 
            else:
                for p in prev_list:
                    c = p.copy()
                    c.append(nums[i])
                    if c not in prev_list:
                        curr_list.append(c)
                prev_list = prev_list + curr_list

        return ans +prev_list
            


        