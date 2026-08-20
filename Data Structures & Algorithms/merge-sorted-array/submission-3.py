class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        for n2 in nums2:
            while m > 0 and n2 > nums1[i]:
                i+=1
                m-=1         
            nums1.insert(i,n2)
            i+=1

        while n > 0:
            nums1.pop()
            n-=1
        return nums1
        