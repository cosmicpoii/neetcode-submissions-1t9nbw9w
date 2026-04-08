class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(1, len(matrix)):
            if target < matrix[row][0]:
                target_row = matrix[row - 1]
                
                l, r = 0, len(matrix[0]) - 1
                
                while l <= r:
                    mid = l + ((r - l) // 2)

                    if target_row[mid] < target:
                        l = mid + 1
                    elif target_row[mid] > target:
                        r = mid - 1
                    else:
                        return True
        return False
