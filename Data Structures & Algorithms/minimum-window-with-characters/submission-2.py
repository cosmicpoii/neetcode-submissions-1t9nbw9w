class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""

        countT = {}
        window = {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        have, need = 0, len(countT)
        res = [-1, -1]
        resLen = float("inf")
        l = 0

        for r in range(len(s)):
            char_s = s[r]
            window[char_s] = 1 + window.get(char_s, 0)

            if char_s in countT and window[char_s] == countT[char_s]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
