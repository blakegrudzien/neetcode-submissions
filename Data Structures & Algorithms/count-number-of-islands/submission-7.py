class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(r,c):
            q = collections.deque()
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            q.append([r,c])
            while q:
                row,col = q.popleft()
                for dr, dc in directions:
                    r = dr+row
                    c = dc+col
                    if rows > r >=0 and cols > c >=0 and (r,c) not in visited and grid[r][c] == "1":
                        q.append([r,c])
                        visited.add((r,c))
            return

        visited = set()
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    visited.add((r,c))
                    bfs(r,c)
                    islands+=1
        return islands 

        