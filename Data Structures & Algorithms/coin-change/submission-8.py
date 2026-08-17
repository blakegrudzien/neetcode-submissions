class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [0] * amount
        print(arr)
        current_value = 0
        if amount == 0:
            return 0
       
        for j in coins:
            if j == amount: return 1 
            if j< amount:
                arr[j] = 1
        i = 2
        print(arr)

        while i*coins[0]<=amount:
            for k in range(len(arr)):
                if arr[k] != 0 and arr[k]<=i:
                    for l in coins:
                        if k + l == amount: 
                            print(arr)
                            return arr[k]+1
                        if k +l < amount and arr[k+l] ==0:
                            arr[k+l] = arr[k]+1
            i+=1
        return -1

        
        
       

          


        


        