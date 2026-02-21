# Note: this question is solved for the leetcode question (https://leetcode.com/problems/reverse-integer/) but it also fit for striver's as well.

class Solution:
    def reverseNumber(self, n):
        INT_MAX = 2147483647

        sign = -1 if n < 0 else 1

        n = abs(n)
        rev = 0

        while n != 0:

            digit = n % 10

            if rev > INT_MAX:
                return 0
            if rev == 214748364 and digit > 7:
                return 0
            
            rev = rev * 10 + digit
            n = n // 10

        return sign * rev