class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            x = 0
            y = cols - 1
            if target >= matrix[row][x] and target <= matrix[row][y]:
                while x <= y:
                    m = (x + y) // 2
                    if matrix[row][m] < target:
                        x = m + 1
                    elif matrix[row][m] > target:
                        y = m - 1
                    else:
                        return True
        
        return False
