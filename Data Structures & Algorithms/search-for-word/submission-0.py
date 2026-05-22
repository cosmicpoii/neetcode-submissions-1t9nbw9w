class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        def dfs(position at now, the ith char of word):
            if all char has been checked:
                return True
            if the position at now is not the target:
                return False

            mark the position as used by "#"

            check up/down/left/right

            recover the position

            return whether find or not
        '''

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[i]
            ):
                return False

            temp = board[r][c]

            board[r][c] = "#"

            found = (
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1)
            )

            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False