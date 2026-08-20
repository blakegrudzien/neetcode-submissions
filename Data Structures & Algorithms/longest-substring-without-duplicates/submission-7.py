class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l = 0
        max_ss = 0
        curr_ss = set()
        for i, r in enumerate(s):

            if r in curr_ss:
                
                while l != i and r != s[l]:
                    curr_ss.remove(s[l])
                    l+=1
                l+=1

            curr_ss.add(r)
            max_ss = max(max_ss, len(curr_ss))
                
        
        return max_ss