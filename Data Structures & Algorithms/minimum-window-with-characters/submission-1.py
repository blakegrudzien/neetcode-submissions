class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        count = {}
        for l in t:
            count[l] = count.get(l,0)+1
        correct = len(count.keys())
        l = 0
        r = 0
        best = s
        
        while r<len(s) and correct != 0:
            if s[r] in count:
                count[s[r]]-=1
                if count[s[r]] == 0:
                    correct-=1
            r+=1
        
        if r == len(s):
            if correct != 0:
                return ""

        
        while r<len(s):
            while correct == 0:
                if r-l < len(best):
                    best = s[l:r]
                if s[l] in count:
                    count[s[l]]+=1
                    if count[s[l]] == 1:
                        correct+=1
                l+=1
            if s[r] in count:
                count[s[r]]-=1
                if count[s[r]] == 0:
                    correct-=1
            r+=1
        while correct == 0:
            if r-l < len(best):
                best = s[l:r]
            if s[l] in count:
                count[s[l]]+=1
                if count[s[l]] == 1:
                    correct+=1
            l+=1
        return best
            
        




        