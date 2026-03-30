class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_nums = sorted(nums)
        res = set()

        for i in range(len(sort_nums)):
            for j in range(i + 1, len(sort_nums)):
                for k in range(j + 1, len(sort_nums)):
                    if sort_nums[i] + sort_nums[j] + sort_nums[k] == 0:
                        temp = [sort_nums[i], sort_nums[j], sort_nums[k]]
                        res.add(tuple(temp))
        return [list(i) for i in res]