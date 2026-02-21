class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        original_x = x

        if x < 0:
            return False

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10

        if original_x == rev:
            return True
        else:
            return False

