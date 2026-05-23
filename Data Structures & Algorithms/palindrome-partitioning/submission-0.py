class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def palindrome(sub):
            return sub == sub[::-1]

        def dfs(start):
            if start == len(s):
                res.append(path.copy())
                return

            for end in range(start, len(s)):
                sub = s[start : end + 1]

                if palindrome(sub):
                    path.append(sub)
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return res