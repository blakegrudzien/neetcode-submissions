class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        def bfs(q, visited):

            directions = [[1,0],[-1,0],[0,-1], [0,1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = dr+row
                    c = dc+col
                    if rows > r >= 0 and cols > c >=0 and heights[r][c] >= heights[row][col] and (r,c) not in visited:
                        q.append([r,c])
                        visited.add((r,c))
            return visited
        
        p_q = collections.deque()
        a_q = collections.deque()
        p_visited = set()
        a_visited = set()
        for i in range(len(heights)):
            p_q.append([i,0])
            p_visited.add((i,0))

            a_q.append([i,len(heights[0])-1])
            a_visited.add((i,len(heights[0])-1))
        

        
        for i in range(len(heights[0])):
            if (0,i) not in p_visited:
                p_q.append([0,i])
                p_visited.add((0,i))
            if (len(heights)-1,i) not in a_visited:
                a_q.append([len(heights)-1,i])
                a_visited.add((len(heights)-1,i))


       
        
  
        return [[r, c] for r, c in  bfs(p_q, p_visited) & bfs(a_q, a_visited)]
  
        


        