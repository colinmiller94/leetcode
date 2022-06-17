class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        min_length = 201

        for string in strs:
            if len(string) < min_length:
                min_length = len(string)

        strs = [string[:min_length] for string in strs]

        end_index = min_length - 1

        # default case
        result = ''

        while end_index >= 0:

            prefix = strs[0]
            if sum([prefix == string for string in strs]) == len(strs):
                return strs[0]

            strs = [string[:-1] for string in strs]
            end_index -= 1

        return ''