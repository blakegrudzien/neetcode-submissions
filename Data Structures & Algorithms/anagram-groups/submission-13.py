class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        key = {}

        for word in strs:
            curr = [0]*26

            for l in word:
                curr[ord(l)- ord('a')] +=1
            
            t = tuple(curr)
            if t in key:
                key[t].append(word)
            else:
                key[t] = []
                key[t].append(word)
        for groups in key.values():
            res.append(groups)
        return res


        