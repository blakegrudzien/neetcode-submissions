class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        i = len(arr)-2
        current_max = arr[i+1]
        temp = 0
        arr[i+1] = -1

        while i >=0:
            current_max = max(current_max, temp)
            temp = arr[i]
            
            arr[i] = current_max
            
            i-=1
        return arr

        