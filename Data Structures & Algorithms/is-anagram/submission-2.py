class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        key = {}
        for l in s:
            if l in key:
                key[l] +=1
            else:
                key[l] = 1
        
        for l in t:
            if l not in key:
                return False
            else:
                key[l]-=1
            if key[l] == 0:
                key.pop(l)
        return True
                

        