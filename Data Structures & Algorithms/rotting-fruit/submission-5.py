class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = []
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    fresh +=1
        
        directions = [[1,0],[-1,0], [0, 1], [0,-1]]
        days = 0
        while q and fresh > 0:
            print(q)
            for i in range(len(q)):
                row, col = q.pop(0)
                print([row,col])
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if len(grid) > r >= 0 and len(grid[0]) > c >= 0 and grid[r][c] == 1 and (r,c) not in visited:
                        q.append([r,c])
                        visited.add((r,c))
                        fresh-=1
            
            days+=1
        if fresh > 0:
            return -1
        return days

        