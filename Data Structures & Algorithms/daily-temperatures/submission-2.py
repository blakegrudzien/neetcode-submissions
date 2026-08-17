class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        h = []
        

        for i in range(len(temperatures)):
            print(h)
            while h and (temperatures[i],0) > h[len(h)-1]:
                (l,j) = h.pop()
                temperatures[j] = i-j
            h.append((temperatures[i],i))
        while h:
            (l,j) = h.pop()
            temperatures[j] = 0

        return temperatures
            
        