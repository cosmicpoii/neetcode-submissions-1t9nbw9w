class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        step 1: set a map to store the number with its characters
        step 2: dfs
        '''

        # 2: [A, B, C], 3: [D, E, F]
        # string: 23, result: [AD, AE, AF, BD, ...]

        if digits == "":
            return []

        res = []
        character_map = {"2": ["a", 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                        '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                        '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        path = []
        def dfs(i):
            if i == len(digits):
                res.append("".join(path))
                return

            digit = digits[i]

            for ch in character_map[digit]:
                path.append(ch)
                dfs(i+1)
                path.pop()
        
        dfs(0)
        return res