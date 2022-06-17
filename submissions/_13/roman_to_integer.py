class Solution:

    @staticmethod
    def numeral_to_number(numeral):
        return {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}[numeral]

    def romanToInt(self, s: str) -> int:

        total = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                total += self.numeral_to_number(s[i])
                break

            current = self.numeral_to_number(s[i])
            next_ = self.numeral_to_number(s[i + 1])

            if next_ > current:
                total += next_ - current
                i += 2
                continue

            total += current
            i += 1

        return total
