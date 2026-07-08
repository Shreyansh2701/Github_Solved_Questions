class Solution:
    def smallestSumSubarray(self, A, N):
        best = A[0]
        ans = A[0]
        for i in range(1,len(A)):
            v1 = best + A[i]
            v2 = A[i]
            best = min(v1, v2)
            ans = min(best, ans)
        return ans
        