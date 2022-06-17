class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numbers = {2: 'abc',
                   3: 'def',
                   4: 'ghi',
                   5: 'jkl',
                   6: 'mno',
                   7: 'pqrs',
                   8: 'tuv',
                   9: 'wxyz', }

        results = []
        for digit in digits:
            if len(results) == 0:
                results = list(numbers[int(digit)])
                continue

            existing = results

            letters = list(numbers[int(digit)])

            results = [combo + letter for combo in existing for letter in letters]

        return results
