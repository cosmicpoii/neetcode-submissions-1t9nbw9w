class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        1. iterate each point to get the distance
        2. use tuple to put each distance and its point to a heap
        3. pop k number of the heap
        '''
        result = []
        heap = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            heapq.heappush(heap, (dist, [x, y]))

        for i in range(k):
            dist, point = heapq.heappop(heap)
            result.append(point)

        return result