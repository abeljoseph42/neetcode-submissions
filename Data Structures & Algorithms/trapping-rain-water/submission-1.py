class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        gapArea = 0

        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            # until height[r] >= height[l] run for loop 
            #between the distance to add to area
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                gapArea += leftMax - height[l]
            
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                gapArea += rightMax - height[r]
        
        return gapArea


        