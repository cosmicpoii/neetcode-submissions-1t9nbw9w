class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        step 1: run DFS from every border "O"
        step 2: mark every border-connected "O" as temporary "T"
        step 3: change remaining "O" to "X"
        step 4: change temporary "T" to "O"
        '''
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != "O"
            ):
                return

            board[r][c] = "T"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"