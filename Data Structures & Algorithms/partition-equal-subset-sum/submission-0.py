class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        goal = total/2
        if max(nums) >= goal:
            if max(nums)==goal:
                return True
            return False
        s = set()
        s.add(nums[len(nums)-1])
        s.add(0)
        

        i = len(nums)-2
        while i>=0:
            temp = s.copy()
            for n in temp:
                if n+nums[i] == goal:
                    return True
                if n+nums[i] < goal:
                    s.add(n+nums[i])
            i-=1
        return False

       

            



        