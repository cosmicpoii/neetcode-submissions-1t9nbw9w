class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        result = []
        for i in nums:
            if i not in output:
                output[i] = 1
            else:
                output[i] += 1
        
        sorted_items = sorted(output.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            result.append(sorted_items[i][0])
        
        return result