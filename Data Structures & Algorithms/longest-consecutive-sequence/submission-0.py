class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        maxim = 1
        i = 1

        for j in range(1, len(nums)):
            if nums[j] - nums[j - 1] == 1:
                i += 1
            elif nums[j] == nums[j - 1]:
                continue
            else:
                maxim = max(i, maxim)
                i = 1

        return max(maxim, i)