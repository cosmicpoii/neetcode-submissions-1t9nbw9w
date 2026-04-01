class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = []

        for i in range(n):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                j += 1

            if j == n:
                result.append(0)
            else:
                result.append(j - i)

        return result