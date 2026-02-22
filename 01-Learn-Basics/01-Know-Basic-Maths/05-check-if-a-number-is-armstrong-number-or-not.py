# Check if the Number is Armstrong:

class Solution:
    def isArmstrong(self, n):
        original_n = n
        temp_n = n
        total_sum = 0

        if n < 0:
            return False

        num_digits = 0

        while temp_n > 0:
            digit = temp_n % 10
            num_digits += 1
            temp_n = temp_n // 10


        while n > 0:
            digit = n % 10
            total_sum += digit**num_digits
            n = n // 10
        
        if total_sum == original_n:
            return True
        else:
            return False