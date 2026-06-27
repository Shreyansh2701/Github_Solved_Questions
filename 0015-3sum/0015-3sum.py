class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        i = 0
        n = len(nums)
        res = []
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            sum1 = -1 * nums[i]
            while(left < right):
                twosum = nums[left] + nums[right]
                if twosum == sum1:
                    result = [nums[i], nums[left], nums[right]]
                    res.append(result)
                    left += 1
                    right -= 1
                    while left<n and nums[left] == nums[left-1] :
                        left += 1
                    while right >= 0 and nums[right] == nums[right+1]:
                        right -= 1
                elif twosum > sum1:
                    right -= 1
                else:
                    left += 1
        return res
                    
            