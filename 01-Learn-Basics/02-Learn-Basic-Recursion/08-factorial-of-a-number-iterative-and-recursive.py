# Factorial of a given number

"""
You are given an integer n. Return the value of n! or n factorial.

Factorial of a number is the product of all positive integers less than or equal to that number.

Example 1
Input: n = 2
Output: 2
Explanation: 2! = 1 * 2 = 2.

Example 2
Input: n = 0
Output: 1
Explanation: 0! is defined as 1.
"""

class Solution:
    def factorial(self, n):
      if n == 1 or n == 0:
        return 1

      return n * self.factorial(n-1)
    
obj1 = Solution()
factorial1 = obj1.factorial(0)
print(factorial1)