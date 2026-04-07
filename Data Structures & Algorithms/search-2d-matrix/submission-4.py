class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            row = mid // n
            col = mid % n
            val = matrix[row][col]
            
            if target < val:
                r = mid - 1
            elif target > val:
                l = mid + 1
            else:
                return True
        
        return False