class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap = {}

        for ch in t:
            hashmap[ch] = hashmap.get(ch, 0) + 1

        low = 0
        count = 0
        minlength = float('inf')
        startIndex = -1

        for high in range(len(s)):
            if hashmap.get(s[high], 0) > 0:
                count += 1

            hashmap[s[high]] = hashmap.get(s[high], 0) - 1

            while count == len(t):
                if high - low + 1 < minlength:
                    minlength = high - low + 1
                    startIndex = low

                hashmap[s[low]] = hashmap.get(s[low], 0) + 1

                if hashmap[s[low]] > 0:
                    count -= 1

                low += 1

        if startIndex == -1:
            return ""

        return s[startIndex:startIndex + minlength]