class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
    
        for i in range(len(nums)):
            temp = target - nums[i]
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        result.append(i)

        return result
        