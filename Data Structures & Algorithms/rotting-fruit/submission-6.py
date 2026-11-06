class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        fresh = 0
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append([r,c])
        days = 0
        if fresh == 0:
            return 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                row,col = q.popleft()
                for dr, dc in directions:
                    r = dr+row
                    c = dc+col
                    if rows > r >=0 and cols > c >= 0 and (r,c) not in visited and grid[r][c] == 1:
                        visited.add((r,c))
                        q.append([r,c])
                        fresh-=1
            days+=1
        if fresh > 0:
            return -1
        return days



        