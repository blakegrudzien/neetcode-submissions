class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        visited = set()
        if amount == 0:
            return 0
        q = collections.deque()
        q.append(0)
        rounds = 1
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                for c in coins:
                    if curr+c not in visited and curr+c<=amount:
                        if curr+c == amount:
                            return rounds
                        q.append(curr+c)
                        visited.add(curr+c)
            rounds+=1
        return -1


            
        
 
        