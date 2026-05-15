# Find Nth root of a number

"""
Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.


Example 1
Input: N = 3, M = 27
Output: 3
Explanation: The cube root of 27 is equal to 3.

Example 2
Input: N = 4, M = 69
Output:-1
Explanation: The 4th root of 69 does not exist. So, the answer is -1.
"""


## BINARY SEARCH APPROACH:
class Solution:
    def NthRoot(self, n, m):

        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2

            if self.NthSquare(mid, n) == m:
                return mid
            elif self.NthSquare(mid, n) < m:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1

    def NthSquare(self, mid, n):
        val = mid ** n
        return val



## LINEAR SEARCH APPROACH
class Solution:
    def NthRoot(self, n, m):
      
        for i in range(m):
            if self.NthSquare(i, n) == m:
                return i
            elif self.NthSquare(i, n) > m:
                break

        return -1

    def NthSquare(self, i, n):
        val = i ** n
        return val