class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        key = {}
        
        for l in s:
            key[l] = key.get(l, 0) +1
        r = 0
        curr = set()
        res = []
        l = 0
        while r < len(s):
            if s[r] not in curr:
                curr.add(s[r])
            key[s[r]] -=1
            if key[s[r]] == 0:
                curr.remove(s[r])
            if not curr:
                curr.clear()
                res.append(r-l+1)
                l = r+1
            r+=1
        return res


            
        