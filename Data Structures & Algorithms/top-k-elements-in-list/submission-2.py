class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mymap = {}
        for i in range(len(nums)):
            if nums[i] not in mymap:
                mymap[nums[i]] = 1
            else:
                mymap[nums[i]] += 1
        
        myarr = []
        for num, count in mymap.items():
            myarr.append([count, num])
        myarr.sort()

        result = []
        while len(result) < k:
            result.append(myarr.pop()[1])
        
        return result
        
        