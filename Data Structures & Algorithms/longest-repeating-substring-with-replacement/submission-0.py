class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        max_freq = 0
        result = 0

        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            max_freq = max(max_freq, count[s[i]])

            while (i - l + 1) - max_freq > k:
                count[s[i]] -= 1
                l += 1
                
            result = max(result, i - l + 1)

        return result