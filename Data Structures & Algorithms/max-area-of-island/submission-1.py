class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def bfs(x, y):
            if min(x,y) < 0 or x == rows or y == cols or grid[x][y] == 0:
                return 0
            count = 0

            grid[x][y] = 0
            count+=1

            count+= bfs(x+1, y)
            count+= bfs(x, y+1)
            count+= bfs(x-1, y)
            count+= bfs(x, y-1)

            return count 
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r,c)
                    max_area = max(max_area, area)
        
        return max_area





        
            



        