class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l = 0
        r = 1
        max_ss = 0
        curr_ss = set()
        curr_ss.add(s[l])
        while r < len(s):
            while s[r] not in curr_ss:
            
                curr_ss.add(s[r])
                r+=1
                if r == len(s):
                    return max(max_ss, r-l)
            max_ss = max(max_ss, len(curr_ss))
          
            while s[l] != s[r]:
                curr_ss.remove(s[l])
                l+=1
            if l != r:
                l+=1
            r+=1
        
        return max(max_ss, r-l)