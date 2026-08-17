class Solution:
    def isPalindrome(self, s: str) -> bool:

        st="".join(c for c in s if (c.isalpha() or c.isnumeric()))
                
        S = st.lower()
        #S = st.strip()
        r = len(S)-1
        l = 0
        print(S)

        while l <= r:
            if S[l] != S[r]:
                return False
            l+=1
            r-=1
        return True