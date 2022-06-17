class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        negative = (dividend < 0 or divisor < 0) and (dividend >= 0 or divisor >= 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 1:
            return max(-dividend, -2 ** 31) if negative else min(dividend, 2 ** 31 - 1)

        total = 0
        power = 1
        power_up = True
        while True:

            if dividend < divisor:
                break

            temp = dividend - divisor ** power

            if temp >= divisor:
                total += divisor ** (power - 1)
                if power_up:
                    power += 1
                dividend = temp
                continue

            if temp >= 0 and temp < divisor:
                total += divisor ** (power - 1)
                break

            power -= 1
            power_up = False

        total = max(-2 ** 31, total) if negative else min(2 ** 31 - 1, total)
        result = total if negative is False else -total

        return result
