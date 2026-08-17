class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        S = sorted(s)
        T = sorted(t)

        for i in range(len(s)):
            if S[i] != T[i]:
                return False
        return True


        