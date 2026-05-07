# Floor and Ceil in Sorted Array

"""
Given a sorted array nums and an integer x. Find the floor and ceil of x in nums. The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, output -1.

Example 1
Input : nums =[3, 4, 4, 7, 8, 10], x= 5
Output: 4 7
Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.


Example 2
Input : nums =[3, 4, 4, 7, 8, 10], x= 8
Output: 8 8
Explanation: The floor of 8 in the array is 8, and the ceiling of 8 in the array is also 8.
"""


nums = [3, 4, 4, 7, 8, 10, 11]
x = 8

n = len(nums)

# ---------------- CEIL ----------------
# CEIL = Largest Number in Array (>=target)
low = 0
high = n - 1
ceil = -1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] >= x:
        ceil = nums[mid]
        high = mid - 1
    else:
        low = mid + 1

# ---------------- FLOOR ----------------

low = 0
high = n - 1
floor = -1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] <= x:
        floor = nums[mid]
        low = mid + 1
    else:
        high = mid - 1


print(f"Floor = {floor}")
print(f"Ceil = {ceil}")