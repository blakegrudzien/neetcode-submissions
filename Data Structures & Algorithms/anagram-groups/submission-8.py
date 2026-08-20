class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer_key = {}

        for s in strs:
            curr_key = [0] * 26
            for l in s:
                curr_key[ord(l)-ord('a')] +=1
            t_key = tuple(curr_key)
            if t_key in answer_key:
                answer_key[t_key].append(s)
            else:
                answer_key[t_key] = [s]

        return list(answer_key.values())
        