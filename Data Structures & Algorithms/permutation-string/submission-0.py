class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1 = {}
        for char in s1:
            count_s1[char] = 1 + count_s1.get(char, 0)

        window = len(s1)
        count_window = {}

        for i in s2[:window]:
            count_window[i] = 1 + count_window.get(i, 0)

        if count_s1 == count_window:
            return True

        for r in range(window, len(s2)):
            count_window[s2[r]] = 1 + count_window.get(s2[r], 0)

            l = r - window
            count_window[s2[l]] -= 1
            if count_window[s2[l]] == 0:
                del count_window[s2[l]]

            if count_s1 == count_window:
                return True

        return False