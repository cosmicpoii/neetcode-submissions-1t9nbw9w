class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        step 1: put all treasure chests, value 0, into a queue
        step 2: use BFS to expand from these treasure chests level by level
        step 3: when we find an INF neighbor, update it to current cell distance + 1
        step 4: add this neighbor to the queue so it can continue spreading the distance
        '''
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    grid[nr][nc] != 2147483647
                ):
                    continue

                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
        