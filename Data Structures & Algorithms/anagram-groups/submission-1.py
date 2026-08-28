class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs:
            sortedStr = ''.join(sorted(s))
            if sortedStr not in result:
                result[sortedStr] = [s]
            else:
                result[sortedStr].append(s)
        
        return list(result.values())

