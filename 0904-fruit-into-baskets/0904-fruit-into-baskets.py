class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low = 0
        high = 0
        n = len(fruits)
        res = -1
        resulthash = {}
        k = 2
        for high in range(n):
            resulthash[fruits[high]] = resulthash.get(fruits[high], 0) + 1
            while len(resulthash) > k:
                resulthash[fruits[low]] = resulthash.get(fruits[low]) - 1
                if resulthash[fruits[low]] == 0:
                    del resulthash[fruits[low]]
                low += 1
            if len(resulthash) < k or len(resulthash) == k:
                length = high-low+1
                res = max(res, length)
        return res

        