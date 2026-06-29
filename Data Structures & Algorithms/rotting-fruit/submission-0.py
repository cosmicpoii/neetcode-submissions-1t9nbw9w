class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        step 1: add all rotten fruits to a deque and count fresh fruits
        step 2: use BFS to spread rotting level by level
        step 3: each BFS level means one minute
        step 4: if all fresh fruits become rotten, return minutes
        step 5: otherwise return -1
        '''

        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        grid[nr][nc] != 1
                    ):
                        continue

                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1
