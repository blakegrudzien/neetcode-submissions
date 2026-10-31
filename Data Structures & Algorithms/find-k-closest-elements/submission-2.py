class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = k

        while r< len(arr) and (abs(arr[r]-x) < abs(arr[l]-x) or (arr[l] == arr[r])) :
            l+=1
            r+=1
        return arr[l:r]

        