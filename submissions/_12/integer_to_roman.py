class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ''

        letters = [[1000, 'M'], [500, 'D'], [100, 'C'], [50, 'L'], [10, 'X'], [5, 'V'], [1, 'I']]

        index = 0
        while num > 0 and index < len(letters):

            computed_num = num - letters[index][0]
            if computed_num < 0:
                index += 1
                continue

            num = computed_num
            roman += letters[index][1]

        replacements = [['VIIII', 'IX'], ['IIII', 'IV'],
                        ['LXXXX', 'XC'], ['XXXX', 'XL'],
                        ['DCCCC', 'CM'], ['CCCC', 'CD']]

        for replacement in replacements:
            roman = roman.replace(replacement[0], replacement[1])

        return roman
