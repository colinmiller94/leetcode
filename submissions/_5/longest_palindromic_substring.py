class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        best = 0
        longest = ''
        for i in range(0, len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > best:
                    best = r - l + 1
                    longest = s[l: r + 1]

                l -= 1
                r += 1

        for i in range(0, len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > best:
                    best = r - l + 1
                    longest = s[l: r + 1]

                l -= 1
                r += 1

        return longest