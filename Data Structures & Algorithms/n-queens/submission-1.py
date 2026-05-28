class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        step 1: use backtracking to place queens row by row
            since each row can only contain one queen, so the state is the current row
            and a list queens where queens[row] = col

        step 2: check whether a queen conflicts with previous queens before putting it at (row, col)
            previous queens:
                a. same col: col == prev_col
                b. same diagonal: abs(row - prev_row) = abs(col - prev_col)

        step 3: where row == n, all queens have been placed successfully, add it to the result
        '''

        res = []
        queens = []

        def is_valid(row, col):
            for prev_row in range(row):
                prev_col = queens[prev_row]

                if col == prev_col:
                    return False

                if abs(row - prev_row) == abs(col - prev_col):
                    return False

            return True

        def dfs(row):
            if row == n:
                board = []
                for col in queens:
                    row_str = "." * col + "Q" + "." * (n - col - 1)
                    board.append(row_str)

                res.append(board)
                return

            for col in range(n):
                if is_valid(row, col):
                    queens.append(col)
                    dfs(row + 1)
                    queens.pop()

        dfs(0)
        return res