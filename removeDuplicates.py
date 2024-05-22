class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Two pointers and keep track of max number (my approach)
        """
        mx = nums[0]
        i = 1
        for j in range(len(nums)):
            if nums[j] > mx:
                nums[i] = nums[j]
                i += 1
                mx = nums[j]
        return i

    def removeDuplicates2(self, nums: List[int]) -> int:
        """
        Others' better solution
        """
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
