class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer_key = {}

        for s in strs:
            curr_key = {}
            for l in s:
                if l in curr_key: 
                    curr_key[l] +=1
                else:
                    curr_key[l] = 1
            curr_frozen = frozenset(curr_key.items())
            if curr_frozen in answer_key:
                answer_key[curr_frozen].append(s)
            else:
                answer_key[curr_frozen] = [s]

        return list(answer_key.values())
        