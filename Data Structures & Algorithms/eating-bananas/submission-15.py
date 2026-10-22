class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(piles, h, check_num):
            count = 0
            for p in piles:
                count += p //check_num
                if p%check_num != 0:
                    count+=1
            if count <=h:
                return True
            return False
        lower = 1
        upper = max(piles)
        best_num = upper

        while lower <= upper:
            mid = (lower + upper)//2

            if check(piles, h, mid):
                best_num = mid
                upper = mid-1
            else:
                lower = mid+1
        return best_num
