class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(row):
            l, r = 0, len(row) - 1
                    
            while l <= r:
                mid = l + ((r - l) // 2)

                if row[mid] < target:
                    l = mid + 1
                elif row[mid] > target:
                    r = mid - 1
                else:
                    return True
            return False
        
        for row in range(1, len(matrix)):
            if target < matrix[row][0]:
                target_row = matrix[row - 1]
                return binary_search(target_row)
        return binary_search(matrix[-1])
