class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(x,y):
            
            rows, cols = len(grid), len(grid[0])
            if min(x, y) <0 or x == rows or y == cols or grid[x][y] == "0":
                return
 
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            
            grid[x][y] = "0"
            for dr, dc in directions:
                bfs(x+dr, y+dc)
            return
       
        count = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                print(grid[r][c])
                if grid[r][c] == "1":
  
                    bfs(r, c)
                    count+=1

        print(grid)
        return count 

        
            


                    

        