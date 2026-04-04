class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0

        for l in range(n):
            min_h = float("inf")
            for r in range(l, n):
                min_h = min(min_h, heights[r])
                res = max(res, min_h * (r - l + 1))

        return res