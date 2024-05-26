class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # my version
        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
        return i
