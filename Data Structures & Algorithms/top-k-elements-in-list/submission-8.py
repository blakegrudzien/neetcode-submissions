class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        key = [[] for i in range(len(nums)+1)]
        ans = []

        for n in nums:
            if n in count:
                count[n] +=1
            else:
                count[n] = 1

        for v in count:
            key[count[v]].append(v)

        i = len(nums) 


        while i >=0:

            while key[i]:
                ans.append(key[i].pop())
            if len(ans) == k:
                return ans
            i-=1
        return ans



        
            
            
            

