class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                curLength = 1
                while num + 1 in numSet:
                    curLength += 1
                    num = num + 1
                longest = max(longest, curLength)
        
        return longest
