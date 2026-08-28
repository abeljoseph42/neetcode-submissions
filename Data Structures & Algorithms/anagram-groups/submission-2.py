class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        myMap = {}

        for string in strs:
            sortString = "".join(sorted(string))
            if sortString in myMap:
                myMap[sortString].append(string)
            else:
                myMap[sortString] = [string]
        
        for key in myMap:
            res.append(myMap[key])
        
        return res