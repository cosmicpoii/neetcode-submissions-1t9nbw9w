class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            temp = nums.pop(i)
            product = 1
            for j in nums:
                product *= j
            result.append(product)
            nums.insert(i, temp)
        return result
