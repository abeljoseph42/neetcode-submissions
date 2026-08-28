class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = []
        duplicate = False
        for i in range(len(nums)):
            if nums[i] not in uniqueNums:
                uniqueNums.append(nums[i])
            else:
                duplicate = True
        
        return duplicate
