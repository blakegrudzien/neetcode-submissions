class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ans_key = set()
        curr_key = set()
        for i, val in enumerate(nums): 
            #print(val)
            curr_key.clear()
            p = i+1
            while p < len(nums):
                #print(curr_key)
                if nums[p] in curr_key:
                    #print("match found ")
                    new_match = [val,nums[p], (val+nums[p]) * -1]
                    new_match.sort()
                    #print(new_match)
           
                    if tuple(new_match) not in ans_key:
                        #print("adding key")
                        ans.append(new_match)
                        ans_key.add(tuple(new_match))
                        #print(ans_key)
                #print(ans)
                
                curr_key.add((nums[p] + val) * -1)
                p+=1
        return list(ans) 
                    


            


        