class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(piles, h, check_num):
            hours_spent = 0
            for p in piles:
                hours_spent+= math.ceil(p / check_num)
            if hours_spent <= h:
                return True
            return False
        

        lower = 1
        upper = max(piles)
        curr_best = upper
        
        while lower <= upper:
            mid = (lower + upper)//2
            if check(piles, h, mid):
                curr_best = mid
                upper = mid-1
            else:
                lower = mid+1
        
        return curr_best