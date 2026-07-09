class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = nums[0]
        minProduct = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            tempMax = max(num, num * maxProduct, num * minProduct)
            minProduct = min(num, num * maxProduct, num * minProduct)
            maxProduct = tempMax
            result = max(result, maxProduct)
        return result