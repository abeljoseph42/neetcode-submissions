class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
        
        maxCount = 0
        for i in range(len(nums)):
            if nums[i] - 1 in seen:
                continue
            else:
                tempCount = 1
                start = nums[i]
                while start + 1 in seen:
                    tempCount += 1
                    start = start + 1
            maxCount = max(maxCount, tempCount)
        
        return maxCount

