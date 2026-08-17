class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        key = []

        for i in nums:
            if i in key:
                return i
            else:
                key.append(i)
        