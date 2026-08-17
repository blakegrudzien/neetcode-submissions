class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        col = len(grid[0])
        
        visited = set()
        q = deque()
        num_fresh = set()


        def add_cell(a,b,grid, num_fresh):
            if min(a,b) < 0 or a == rows or b == col or (a,b) in visited or grid[a][b] != 1:
                return
            visited.add((a,b))
            q.append([a,b])
            num_fresh.remove((a,b))



       



        for r in range(rows):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
                if grid[r][c] == 1:
                    num_fresh.add((r,c))
        seconds = 0

        



        while q:
            seconds+=1
            for i in range(len(q)):

                a,b = q.popleft()

                grid[a][b] = 2

                add_cell(a+1,b,grid, num_fresh)
                add_cell(a,b-1,grid, num_fresh)
                add_cell(a,b+1,grid, num_fresh)
                add_cell(a-1,b,grid, num_fresh)
            

        
        if num_fresh:
            print(num_fresh)
            return -1
        else:
            return max(seconds-1,0) 




        