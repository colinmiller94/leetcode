class Solution:
    def convert(self, s, numRows):
        down = True
        y = 0
        results = [[] for i in range(numRows)]
        for c in s:
            results[y].append(c)
            if y == numRows - 1:
                down = False

            if y == 0:
                down = True

            if numRows == 1:
                continue

            if down:
                y +=1
                continue
            y -= 1

        return ''.join([char for res in results for char in res])