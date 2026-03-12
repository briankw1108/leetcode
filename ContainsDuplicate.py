# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def containDuplicates(self, nums: List[int]) -> bool:
        return not len(nums) == len(set(nums))


# class Solution:
#     def containDuplicates(self, nums: List[int]) -> bool:
#         hashset = set()
#         for x in nums:
#             if x in hashset:
#                 return True
#             hashset.add(x)
#         return False
# The time complexity of this approach is O(n), where n is the length of the array.


# class Solution:
#     def containDuplicates(self, nums: List[int]) -> bool:
#         nums.sort()
#         n = len(nums)
#         for i in range(1, n):
#             if nums[i-1] == nums[i]:
#                 return True
#         return False
# The time complexity of this approach is O(n log n), where n is the length of the array.
