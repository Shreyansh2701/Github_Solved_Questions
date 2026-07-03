class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_water_stored = 0
        while left < right:
            current_min_height = min(height[left], height[right])
            current_stored_water =  current_min_height * (right-left)
            max_water_stored = max(max_water_stored, current_stored_water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water_stored
