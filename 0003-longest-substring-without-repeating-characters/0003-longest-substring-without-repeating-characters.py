class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        high = 0
        n = len(s)
        res = 0
        resulthash = {}
        for high in range(n):
            resulthash[s[high]] = resulthash.get(s[high],0) + 1
            k = high - low + 1
            while len(resulthash) < k:
                resulthash[s[low]] = resulthash.get(s[low]) - 1
                if resulthash[s[low]] == 0:
                    del resulthash[s[low]]
                low += 1
                k = high - low + 1
            if len(resulthash) == k:
                length = high - low + 1
                res = max(res,length)    
        return res