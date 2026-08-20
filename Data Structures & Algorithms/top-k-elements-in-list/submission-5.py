class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        for n in nums:
            
            count[n] +=1
        answer = sorted(count, key = count.get, reverse= True)
        return answer[0:k]
            
            
            

