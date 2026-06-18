class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        step 1: traverse every cell in the grid
        step 2: when we find cell called "1", run DFS to calculate this island's area
        step 3: mark visited cell as "0" to avoid counting them again
        step 4: update the maximum area and return it
        '''
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            area = 1

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0
            ):
                return 0

            grid[r][c] = 0

            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(max_area, area)

        return max_area