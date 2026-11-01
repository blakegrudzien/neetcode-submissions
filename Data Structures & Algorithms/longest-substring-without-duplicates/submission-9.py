class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        window = set()
        curr_best = 0

        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                r+=1  
            else:
                curr_best = max(curr_best, len(window))
                while s[l] != s[r]:
                    window.remove(s[l])
                    l+=1
                l+=1
                r+=1
        curr_best = max(curr_best, len(window)) 
        return curr_best
        