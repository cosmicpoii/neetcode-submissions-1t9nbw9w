class Solution:

    def encode(self, strs: List[str]) -> str:
        temp_str = ""
        for i in strs:
            temp_str += str(len(i)) + "#" + i
        return temp_str

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j
        
        return result
