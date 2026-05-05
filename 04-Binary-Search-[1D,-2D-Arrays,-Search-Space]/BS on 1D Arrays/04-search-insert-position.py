# Search insert position

"""
Given a sorted array of nums consisting of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Example 1
Input: nums = [1, 3, 5, 6], target = 5
Output: 2

Explanation: The target value 5 is found at index 2 in the sorted array. Hence, the function returns 2.


Example 2
Input: nums = [1, 3, 5, 6], target = 2
Output: 1

Explanation: The target value 2 is not found in the array. However, it should be inserted at index 1 to maintain the sorted order of the array.
"""




nums = [1, 3, 5, 6]
target = 5

n = len(nums)
ans = n

low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] >= target:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print("Expected Output: 2")
print(f"Your Output: {ans}")