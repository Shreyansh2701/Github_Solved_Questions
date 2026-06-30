class Solution:
    def longestKSubstr(self, s, k):
        low = 0
        high = 0
        res = float('-inf')
        resulthash = {}
        n = len(s)
        for high in range(n):
            resulthash[s[high]] = resulthash.get(s[high],0) + 1
            while len(resulthash) > k:
                resulthash[s[low]] = resulthash.get(s[low]) - 1
                if resulthash[s[low]] == 0:
                    del resulthash[s[low]]
                low += 1
            if len(resulthash) == k:
                length = high - low + 1
                res = max(res, length)
        if res == float('-inf'):
            return -1
        else:
            return res