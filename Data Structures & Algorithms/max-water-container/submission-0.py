class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while l < r:
            height = min(heights[l], heights[r])
            area = height * (r - l)
            if area > maxArea:
                maxArea = area

            if height == heights[l]:
                l += 1
            elif height == heights[r]:
                r -= 1

        return maxArea