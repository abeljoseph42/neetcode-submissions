class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fmap = defaultdict(int)
        maxLen = 0
        l = 0

        for r in range(len(s)):
            fmap[s[r]] += 1

            while fmap[s[r]] > 1:
                fmap[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen

        