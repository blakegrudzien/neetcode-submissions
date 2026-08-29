class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        c = []
        for i in range(len(nums)):
            curr_list = []
            for a in ans:
                c = a.copy()
                c.append(nums[i])
                c.sort()
                if c not in ans:
                    curr_list.append(c)           
            ans = ans + curr_list
        return ans 
            


        