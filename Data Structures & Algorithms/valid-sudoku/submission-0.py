class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for i in range(len(board)):
            rowSet = set()
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] not in rowSet:
                        rowSet.add(board[i][j])
                    else:
                        return False
        
        #columns
        for i in range(len(board)):
            colSet = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                else:
                    if board[j][i] not in colSet:
                        colSet.add(board[j][i])
                    else:
                        return False
            
        #square
        for k in range(len(board)):
            squareSet = set()
            for i in range(3):
                for j in range(3):
                    row = (k // 3) * 3 + i
                    col = (k % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    else:
                        if board[row][col] not in squareSet:
                            squareSet.add(board[row][col])
                        else:
                            return False
        
        return True
        
