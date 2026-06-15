class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        step 1: traverse every cell in the grid
        step 2: when we find a land cell "1", count it as a new island
        step 3: run DFS from this cell to mark all connected land cells as visisted
        step 4: continue scanning the grid and return the total number of islands
        '''

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] != "1"
            ):
                return

            grid[r][c] = "0"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands