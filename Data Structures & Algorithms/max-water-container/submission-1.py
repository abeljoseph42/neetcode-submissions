class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        i, j = 0, len(heights) - 1

        while i < j:
            base = j - i
            minHeight = min(heights[i], heights[j])
            area = base * minHeight
            maximum = max(maximum, area)

            if heights[i] < heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
                j -= 1

        return maximum
            
