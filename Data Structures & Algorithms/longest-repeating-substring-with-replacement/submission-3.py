class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k >= len(s):
            return len(s)

        key = {}

        l = 0
        for i in range(k):
            key[s[i]] = key.get(s[i], 0) + 1

        r = k
        while r< len(s):

            key[s[r]] = key.get(s[r], 0) + 1

            if (r-l+1) > (max(key.values()) + k):
  
                key[s[l]] = key.get(s[l])-1
                l+=1
                r+=1
                
            else:

                r+=1
            
        return r-l


        