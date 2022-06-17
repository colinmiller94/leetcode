class Solution:

    def reverse(self, x):

        total = 0

        sign = 1
        if x < 0:
            sign = -1

        x = abs(x)

        while x > 0:
            total *= 10
            total += x % 10

            if total * sign >= 2 ** 31 - 1 or total * sign <= -1 * 2 ** 31:
                return 0

            x = x // 10

        return total * sign
