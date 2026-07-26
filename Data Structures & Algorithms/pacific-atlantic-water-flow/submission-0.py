class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        step 1: create a visited set for each ocean
        step 2: run DFS from all Pacific border cells
        step 3: run DFS from all Atlantic border cells
        step 4: in DFS, move from lower cells to higher or equal cells
        step 5: return the intersection of the two visited sets as [r, c]
        '''

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    (nr, nc) in visited or
                    heights[nr][nc] < heights[r][c]
                ):
                    continue

                dfs(nr, nc, visited)

        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res