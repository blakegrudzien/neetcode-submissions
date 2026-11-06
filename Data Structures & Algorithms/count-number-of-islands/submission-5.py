class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid, r, c):
            q = [[r, c]]
            visited = set(tuple((r,c)))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            while q:
                for i in range(len(q)):
                    temp_r, temp_c = q.pop()
                    for dr, dc in directions:
                        if len(grid) > (temp_r + dr) >= 0 and len(grid[0]) > temp_c + dc >= 0 and grid[dr+temp_r][dc+temp_c] == '1' and tuple((temp_r + dr, temp_c + dc)) not in visited:
                            q.append([temp_r+dr,temp_c+dc])
                            visited.add(tuple((r,c)))
                    grid[temp_r][temp_c] = "0"


        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(grid, r, c)
                    islands +=1
        return islands 

        