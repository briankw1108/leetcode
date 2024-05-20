class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

        Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

        * Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
        * Return k.

        My first attempt.
        """
        n = len(nums)
        neq = []
        k = 0
        for i in range(n):
            if nums[i] != val:
                neq.append(nums[i])
                k += 1
        for i in range(k):
            nums[i] = neq[i]
        return k

    def removeElement2(self, nums: List[int], val: int) -> int:
        """
        Two pointers approach.
        """
        n = len(nums)
        k = 0
        i = 0
        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                k += 1
                i += 1
        return k
                
