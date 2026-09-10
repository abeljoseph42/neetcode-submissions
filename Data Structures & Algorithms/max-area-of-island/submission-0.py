class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1:
                return 0
            area = 1
            grid[row][col] = 0

            area += dfs(row + 1, col) #down
            area += dfs(row, col - 1) #left
            area += dfs(row - 1, col) #right
            area += dfs(row, col + 1) #up
            return area
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    maxArea = max(maxArea, area)
        
        return maxArea
        

