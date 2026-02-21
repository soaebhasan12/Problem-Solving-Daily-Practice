import math

class Solution:
    def countDigit(self, n):
        if n > 0:
            numDigits = math.floor(math.log10(n)) + 1
            return numDigits