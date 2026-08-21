class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        if nums[l] <= nums[r]:
            return nums[l]


        while l< r:
            print(l)
            print(r)
            if nums[l] < nums[l-1]:
                print("hit left")
                return nums[l]
            if nums[r] < nums[r-1]:
                print("hit right")
                return nums[r]
            m = (l+r)//2
            if nums[m] < nums[m-1]:
                print("hit mid")
                return nums[m]
            if nums[m] > nums[l]:
                l = m+1

            elif nums[m] < nums[l]:
                r = m-1
        #print("didn't hit", l, " ", r, " ", m)
        return l
            
            

        