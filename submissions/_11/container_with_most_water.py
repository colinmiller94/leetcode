class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        best = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            if area > best:
                best = area

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return best
