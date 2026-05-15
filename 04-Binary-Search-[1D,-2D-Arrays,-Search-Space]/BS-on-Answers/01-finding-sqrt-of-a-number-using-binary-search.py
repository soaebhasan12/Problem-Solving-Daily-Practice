# Find square root of a number

"""
Given a positive integer n. Find and return its square root. If n is not a perfect square, then return the floor value of sqrt(n).

Example 1
Input: n = 36
Output: 6
Explanation: 6 is the square root of 36.

Example 2
Input: n = 28
Output: 5
Explanation: The square root of 28 is approximately 5.292. So, the floor value will be 5.
"""

## BINARY SEARCH APPROACH:
class Solution:
    def floorSqrt(self, n: int) -> int:

        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2

            if mid * mid <= n:
                low = mid + 1
            else:
                high = mid - 1
        
        return high



## LINEAR SEARCH APPROACH:
class Solution:
    def floorSqrt(self, n: int) -> int:
        ans = 0
        for i in range(n):
            if i * i <= n:
                ans = i
            else:
                break
        
        return ans