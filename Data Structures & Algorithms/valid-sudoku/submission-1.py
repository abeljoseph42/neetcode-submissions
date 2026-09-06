class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for i in range(len(board)):
            rowSet = set()
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowSet:
                    return False
                rowSet.add(board[i][j])
        
        #cols
        for i in range(len(board)):
            colSet = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] in colSet:
                    return False
                colSet.add(board[j][i])
        
        #square
        for sq in range(len(board)):
            sqSet = set()
            for i in range(3):
                for j in range(3):
                    row = (sq // 3) * 3 + i
                    col = (sq % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in sqSet:
                        return False
                    sqSet.add(board[row][col])
        
        return True
