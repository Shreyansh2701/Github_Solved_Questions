class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxlength = 0
        zeros = 0
        n = len(nums)
        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if zeros <= k:
                length = right - left + 1
                maxlength = max(maxlength, length)
        return maxlength