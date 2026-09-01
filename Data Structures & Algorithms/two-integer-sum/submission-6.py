class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, j in enumerate(nums):
            difference = target - j
            if difference in seen:
                return [seen[difference], i]
            else:
                seen[j] = i