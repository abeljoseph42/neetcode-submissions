class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sMap = {}
        for i in range(len(s)):
            letter = s[i]
            if letter in sMap:
                sMap[letter] += 1
            else:
                sMap[letter] = 1
        
        tMap = {}
        for i in range(len(t)):
            letter = t[i]
            if letter in tMap:
                tMap[letter] += 1
            else:
                tMap[letter] = 1
        
        return sMap == tMap
        