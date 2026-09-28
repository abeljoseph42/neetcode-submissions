class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1

        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        
        if not(top <= bot):
            return False

        row = (top + bot) // 2
        x = 0
        y = cols - 1

        while x <= y:
            m = (x + y) // 2
            if matrix[row][m] < target:
                x = m + 1
            elif matrix[row][m] > target:
                y = m - 1
            else:
                return True
        
        return False
