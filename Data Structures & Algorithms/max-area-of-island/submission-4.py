class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(r,c):
            units = 1
            directions = [[1,0],[0,1], [-1,0], [0,-1]]
            q = collections.deque()
            q.append([r,c])
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = dc + col
                    if len(grid) > r >= 0 and len(grid[0]) > c >= 0 and grid[r][c] == 1:
                        q.append([r,c])
                        grid[r][c] = 0
                        units+=1
            return units

        rows = len(grid)
        cols = len(grid[0])
        max_size = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    grid[r][c] = 0
                    max_size = max(max_size, bfs(r,c))
        return max_size
                    
        