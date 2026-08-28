class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}

        for i,j in enumerate(nums):
            difference = target - j
            if difference in myMap:
                return [myMap[difference], i]
            else:
                myMap[j] = i