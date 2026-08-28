class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            multVal = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                multVal *= nums[j]
            res.append(multVal)
        
        return res
        