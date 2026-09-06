class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        suffix = [1] * n
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        
        output = [0] * n
        for i in range(len(nums)):
            product = prefix[i] * suffix[i]
            output[i] = product

        return output

