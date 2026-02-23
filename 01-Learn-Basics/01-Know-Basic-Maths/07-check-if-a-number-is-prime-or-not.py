# Check if a number is prime or not

"""
Problem Statement: Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2..
"""

class Solution:
    def isPrime(self, n):
      if n == 0 or n == 1:
        return False
      
      for i in range(2, int(n**0.5)+1):
        if n % i == 0:
          return False
        else:
          return True