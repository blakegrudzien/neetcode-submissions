class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(piles, h, check_num):
            count = 0
            for v in piles:
                count += v//check_num
                if v%check_num != 0:
                    count+=1
            if count <=  h:
                return True
            return False

        lower = 1
        upper = max(piles)
        curr_best = upper

        while lower <= upper:
            mid = (upper+lower)//2
            if check(piles, h, mid):
                curr_best = mid
                upper = mid-1
            else:
                lower = mid+1
        return curr_best

                