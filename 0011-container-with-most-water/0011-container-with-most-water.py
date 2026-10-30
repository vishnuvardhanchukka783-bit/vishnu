
class Solution:
    def maxArea(self, height: list[int]) -> int:

        left = 0
        right = len(height) - 1

        max_water = 0

        while left < right:

            # Calculate width
            width = right - left

            # Find minimum height
            h = min(height[left], height[right])

            # Calculate water area
            area = width * h

            # Update maximum area
            max_water = max(max_water, area)

            # Move the smaller height pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water     