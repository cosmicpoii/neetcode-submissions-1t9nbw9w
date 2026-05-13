class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        result = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            # choose that number
            subset.append(nums[i])
            dfs(i + 1)

            # donot choose that number
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result
