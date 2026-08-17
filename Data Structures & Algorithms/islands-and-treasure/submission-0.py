class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        col = len(grid[0])

        visited = set()
        q = deque()


        def add_nums(a,b,visited, grid, rows, col):
            if a < 0 or a == rows or b < 0 or b == col or (a,b) in visited or grid[a][b] == -1:
                return
            visited.add((a,b))
            q.append([a,b])

         

        for r in range(rows):
            for c in range(col):
                if grid[r][c] == 0:
                    visited.add((r,c))  
                    q.append([r,c])

        dist = 0

        while q:
            for i in range(len(q)):
                a,b = q.popleft()
                grid[a][b] = dist

                add_nums(a+1,b,visited,grid, rows, col)
                add_nums(a-1,b,visited,grid, rows, col)
                add_nums(a,b+1,visited,grid, rows, col)
                add_nums(a,b-1,visited,grid, rows, col)
            dist+=1

            
    

       


                     
        