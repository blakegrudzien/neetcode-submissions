class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        count = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(x,y):
            
            if min(x, y) <0 or x == rows or y == cols or grid[x][y] == "0":
                return
 
            grid[x][y] = "0"
            for dr, dc in directions:
                dfs(x+dr, y+dc)
       
        

        for r in range(rows):
            for c in range(cols):
                print(grid[r][c])
                if grid[r][c] == "1":
  
                    dfs(r, c)
                    count+=1


        return count 

        
            


                    

        