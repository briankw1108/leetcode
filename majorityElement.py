class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Given an array nums of size n, return the majority element.
        The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
        
        Example 1:
        Input: nums = [3,2,3]
        Output: 3
        
        Example 2:
        Input: nums = [2,2,1,1,1,2,2]
        Output: 2

        My approach is using hashmap to store freqency of occurance of each unique element in the array 
        """
        n = len(nums)
        thresh = n//2
        freq = {}
        majority = None
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
            majority = [k for k,v in freq.items() if v>thresh]
            if len(majority)>0:
                break
        return majority[0]

    def majorityElement2(self, nums: List[int]) -> int:
        """
        This one uses `Moore Voting Algorithm`, which is based on the fact that 
        if there is a majority element in an array, it will always remain in the lead, 
        even after encountering other elements.

        1. create variable `count` and `candidate`, and set `count` as 0 and `candidate` as None,
        2. iterate through the list,
        3. assign `candidate` as `num[i]` if `count` == 0,
        4. if `nums[i]` == `candidate`m=, `count` = `count` + 1, else `count` = `count` - 1
        5. return `candidate`
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
