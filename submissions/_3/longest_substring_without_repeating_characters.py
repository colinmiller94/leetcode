class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0

        used = {}

        # pointer for start of longest string
        l = 0

        for i, char in enumerate(s):

            if char in used and l <= used[char]:
                l = used[char] + 1

            else:
                max_length = max(max_length, i - l + 1)

            used[char] = i

        return max_length