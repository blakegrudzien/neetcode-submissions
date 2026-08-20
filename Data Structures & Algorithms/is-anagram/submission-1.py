class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_key = {}

        for l in s:
            if l in s_key:
                s_key[l] +=1
            else:
                s_key[l] = 1
        
        for l in t:
            if l in s_key:
                s_key[l] -=1
            else:
                return False
        for v in s_key.values():
            if v != 0:
                return False
        return True
        