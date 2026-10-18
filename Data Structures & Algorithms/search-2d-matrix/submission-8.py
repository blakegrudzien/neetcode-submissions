class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get_val(x):
            val = matrix[x//len(matrix[0])][ x % len(matrix[0])]
            return val

        

        l = 0
        r = len(matrix) * len(matrix[0])-1
        while l <= r:
            midpoint = (l+r)//2
            midpoint_val = get_val(midpoint)

            if midpoint_val == target:
                return True 
            if midpoint_val > target:
                r = midpoint-1
            else:
                l = midpoint+1
        return False




        