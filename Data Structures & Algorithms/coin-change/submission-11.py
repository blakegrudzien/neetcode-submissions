class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        a = [0] * amount

        for c in coins:
            if c == amount:
                return 1
            if c < amount:
                a[c] = 1

        for i in range(2,amount+1):
            for index in range(0,amount):
                if a[index] == i-1:
                    for c in coins:
                        if index+c == amount:
                            print(a)
                            return i
                        elif index+c < amount and a[index+c] == 0:
                            a[index+c] = i

        print(a)
        return -1


        