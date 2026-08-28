class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        for i in range(len(s)):
            if s[i] in sMap:
                sMap[s[i]] += 1
            else:
                sMap[s[i]] = 1
        
        for j in range(len(t)):
            if t[j] in tMap:
                tMap[t[j]] += 1
            else:
                tMap[t[j]] = 1
        
        return sMap == tMap
        