class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()
        def dfs(row, col):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != "O" or (row,col) in seen:
                return
            seen.add((row,col))

            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            dfs(row - 1, col)

            

        for col in range(len(board[0])):
            row = 0
            if board[row][col] == "O":
                dfs(row,col)
        
        for col in range(len(board[0])):
            row = len(board) - 1
            if board[row][col] == "O":
                dfs(row,col)
        
        for row in range(len(board)):
            col = 0
            if board[row][col] == "O":
                dfs(row,col)
        
        for row in range(len(board)):
            col = len(board[0]) - 1
            if board[row][col] == "O":
                dfs(row,col)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row,col) not in seen:
                    board[row][col] = "X"
        
        

"""
        m = len(board) - 1
        n = len(board[0]) - 1

        for row in range(len(board)):
            if row == 0 or row == m:
                for col in range(len(board[0])):
                    #
            else:
                for col in range(len(board[0])):
                    if col == 0 or col == n:
                        #
                    else:
                        continue
"""
