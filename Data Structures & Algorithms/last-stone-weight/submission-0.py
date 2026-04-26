class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use heap to pop the most largest number and compare them
        # because heap in python only support min heap, so put each number's negative number
        max_heap = []
        for i in stones:
            max_heap.append(-i)
        heapq.heapify(max_heap)

        while len(max_heap)>1:
            y = -heapq.heappop(max_heap) # the largest number
            x = -heapq.heappop(max_heap)

            if x != y:
                heapq.heappush(max_heap, -(y - x))

        if max_heap:
            return -max_heap[0]
        else:
            return 0