class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        key = []
        
        for num in nums:
            if len(key) < 1:
                key.append(num)
            else:
                if num > key[len(key)-1]:
                    key.append(num)
                else:

                 
                    i = len(key)-2
                    while i >= 0:
                        if num > key[i]:
                            key[i+1] = min(key[i+1], num)
                            break
                        i-=1
                    key[0] = min(key[0],num)
                
        return len(key)