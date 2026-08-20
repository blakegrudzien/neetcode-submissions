class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer_key = defaultdict(list)

        for s in strs:
            curr_key = [0] * 26
            for l in s:
                curr_key[ord(l)-ord('a')] +=1
            answer_key[tuple(curr_key)].append(s)
    
        return list(answer_key.values())
        