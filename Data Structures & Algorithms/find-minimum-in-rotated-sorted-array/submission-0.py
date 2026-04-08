class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + ((r - l) // 2)
            if nums[r] < nums[mid]:
                # minimum in the right of mid
                l = mid + 1

            else:
                # nums[mid] < nums[r]
                # minimum is nums[mid] or in the left of mid
                r = mid

        return nums[l]