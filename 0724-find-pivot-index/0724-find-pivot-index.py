class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
       left = 0
       right = 0
       totalsum = 0
       for i in range(len(nums)):
        totalsum += nums[i]
       if totalsum-nums[0] == 0:
        return 0
       for i in range(1, len(nums)):
        left += nums[i-1]
        right = totalsum - nums[i] - left
        if left == right:
            return i
       return -1