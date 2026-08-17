class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed):
            time = 0
            for pile in piles:
                time += (pile + speed - 1) // speed  # Calculate the time needed with the current speed
            return time <= h
       
    
        l = 1 
        r = max(piles)
        

        while r>l:
            mid = (r+l) // 2

            if can_finish(mid):
                r = mid
            else:
                l = mid + 1           
        return l
        

            

                



        