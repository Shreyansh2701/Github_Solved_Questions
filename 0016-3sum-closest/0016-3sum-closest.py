class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0
        n = len(nums)
        res = 0
        max_diff = float('inf')
        for i in range(n-2):
            left = i + 1
            right = len(nums) - 1
            
            while(left < right):
                total = nums[i] + nums[left] + nums[right]
                diff = abs(total - target)
                if diff < max_diff:
                    max_diff = diff
                    res = total
                    
                if total > target:
                    right -= 1
                else:
                    left += 1
        return res
                    
            