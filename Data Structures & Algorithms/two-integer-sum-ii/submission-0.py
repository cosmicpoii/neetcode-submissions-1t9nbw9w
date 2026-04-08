class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(numbers)):
            temp = target - numbers[i]
            for j in range(len(numbers)):
                if i != j and numbers[j] == temp:
                    result.extend([numbers[i], numbers[j]])
                    return result
