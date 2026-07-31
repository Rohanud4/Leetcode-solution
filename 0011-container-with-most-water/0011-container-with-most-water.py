class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            if height[left] < height[right]:
                h = height[left]
            else:
                h = height[right]

            width = right - left
            area = h * width

            if area > result:
                result = area

            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return result