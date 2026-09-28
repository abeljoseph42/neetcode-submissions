class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        # while hour < h
        # max k = bigges pile, min k = 1
        # ceil(x/k) = 
        minK = 1
        maxK = max(piles)

        while minK < maxK:
            midK = (minK + maxK) // 2

            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/ midK)
            
            if hours > h:
                minK = midK + 1
            else:
                maxK = midK
        
        return maxK
