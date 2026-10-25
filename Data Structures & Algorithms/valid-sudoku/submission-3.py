class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        digits = []

        mini_squares = [[0,0],[3,0],[6,0],[0,3],[3,3],[6,3],[0,6],[3,6],[6,6]]

        for r,c  in mini_squares:
            print(board[r][c])
            mini_square = []
            for i in range(3):
                for j in range(3):
                    
                    if board[r+i][c+j] in mini_square:
                        return False
                    if board[r+i][c+j] != ".":
                        mini_square.append(board[r+i][c+j])

        for i in range(9):
            horizontal = []
            for v in board[i]:
                if v in horizontal:
                    return False
                if v != ".":
                    horizontal.append(v)
        
        for j in range(9):
            vertical = []
            for k in range(9):
                v = board[k][j]
                if v in vertical:
                    return False
                if v != ".":
                    vertical.append(v)
        return True
                


        