class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        low = 0
        maxFreq = 0
        res = 0

        for high in range(len(s)):
            count[s[high]] = count.get(s[high], 0) + 1
            maxFreq = max(maxFreq, count[s[high]])
            length = high - low + 1
            diff = length - maxFreq
            while diff > k:
                count[s[low]] = count.get(s[low]) - 1
                low += 1
                length = high - low + 1
                diff = length - maxFreq

            res = max(res, high - low + 1)

        return res