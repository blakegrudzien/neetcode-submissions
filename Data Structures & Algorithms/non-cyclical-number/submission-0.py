class Solution:
    def isHappy(self, n: int) -> bool:

        visited = []
        
        while n not in visited:
            if n == 1:
                return True
            visited.append(n)
            x = 0
            sn = str(n)
            for s in sn:
                x+= int(s) * int(s)
            n = x
        return False
        

            


        