class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1,0], [0, 1], [-1,0], [0,-1]]
        visited = []
        rows = len(board)
        cols = len(board[0])

        def dfs(visited, r, c, substring):
            if min(r,c) <0 or r==len(board) or c == len(board[0]) or board[r][c] != substring[0] :
                return
          
            
            if len(substring) == 1:
           
                return True
            for dr, dc in directions:
                if [dr+r, dc+c] not in visited:
                    visited.append([r,c])
                    if dfs(visited, dr+r, dc+c, substring[1:]):
                        return True
                    visited.pop()
            
            return

        for r in range(rows):
            for c in range(cols):
                
                if board[r][c] == word[0]:
                    if dfs(visited, r, c, word):
                        return True
        
        return False
        
        
            
            

        