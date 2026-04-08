class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bound = max(piles)
        
        if len(piles) == h:
            return bound

        for j in range(1, bound + 1):
            total = 0
            for i in piles:
                total += math.ceil(i / j)
            if total <= h:
                return j