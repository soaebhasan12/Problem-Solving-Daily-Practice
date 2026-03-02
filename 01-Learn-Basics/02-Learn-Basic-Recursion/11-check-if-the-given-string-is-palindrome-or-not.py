# Check if String is Palindrome or Not

"""
Given a string s, return true if the string is palindrome, otherwise false.

A string is called palindrome if it reads the same forward and backward.

Example 1
Input : s = "hannah"
Output : true
Explanation : The string when reversed is --> "hannah", which is same as original string , so we return true.

Example 2
Input : s = "aabbaA"
Output : false
Explanation : The string when reversed is --> "Aabbaa", which is not same as original string, So we return false.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[right] == s[left]:
                left += 1
                right -= 1
            elif s[right] != s[left]:
                return False
        return True