class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            num = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                num = nums[j] * num
            output.append(num)
        
        return output