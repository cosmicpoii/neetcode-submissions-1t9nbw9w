class Solution:
    from math import ceil
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        # mid = l + (r - l + 1)

        while l < r:
            mid = l + ((r - l) // 2)
            total = 0

            for pile in piles:
                total += math.ceil(pile / mid)
            if total <= h:
                r = mid
            else:
                l = mid + 1

        return l