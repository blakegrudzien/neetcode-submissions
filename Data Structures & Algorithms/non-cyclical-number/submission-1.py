class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        curr = 0
        while n != 1:
            s = str(n)
            n = 0
            for i in range(len(s)):
                n += int(s[i]) * int(s[i])
            if n in visited:
                return False
            visited.add(n)
        return True
            


        
        

            


        