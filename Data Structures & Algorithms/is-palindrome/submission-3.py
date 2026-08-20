class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l< r:
            while l < r and not s[l].isnumeric() and not s[l].isalpha():
                l+=1
            while l < r and not s[r].isnumeric() and not s[r].isalpha():
                r-=1
            print(s[l])
            print(s[r])
            if s[l].isalpha() and s[r].isalpha():
                if s[l].lower() != s[r].lower():
                    return False
            else:
                if s[l] != s[r]:
                    return False
            l +=1
            r -=1
        return True