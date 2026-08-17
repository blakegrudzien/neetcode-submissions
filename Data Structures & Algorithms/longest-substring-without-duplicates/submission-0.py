class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        key = set()
        max_length = 0

        for r in range(len(s)):
            if s[r] in key:
                while s[r] in key:
                    key.remove(s[l])
                    l+=1
            key.add(s[r])
            max_length = max(max_length,(r-l+1))
            r+=1

                
        return max_length
            


        