class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for i in range(len(nums)):
            if nums[i] in freqMap:
                freqMap[nums[i]] += 1
            else:
                freqMap[nums[i]] = 1
        
        arr = []
        for num, count in freqMap.items():
            arr.append([count, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res