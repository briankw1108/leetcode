class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Given an integer array nums, rotate the array to the
        right by k steps, where k is non-negative.
        
        Example 1:
        Input: nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
        Explanation:
        rotate 1 steps to the right: [7,1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,1,2,3,4]
        
        Example 2:
        Input: nums = [-1,-100,3,99], k = 2
        Output: [3,99,-1,-100]
        Explanation: 
        rotate 1 steps to the right: [99,-1,-100,3]
        rotate 2 steps to the right: [3,99,-1,-100]
        Do not return anything, modify nums in-place instead.

        My approach is that 
        1. when k < len(nums), place last k elements before first n-k elements,
        2. when k >= len(nums), iterate k times to place last element before first n-k elements
        """
        n = len(nums)
        if k < n:
            front, end = nums[n-k:], nums[0:n-k]
            nums[0:len(front)] = front
            nums[len(front):] = end
        else:
            for i in range(k):
                first = nums[-1]
                rest = nums[0:n-1]
                nums[0] = first
                nums[1:] = rest


  def rotate2(self, nums: List[int], k: int) -> None:
      """
      To rotate the array in-place, we can follow these steps:
      
      1. Reverse the entire array,
      2. Reverse the first k elements,
      3. Reverse the remaining n - k elements.
      This method rearranges the elements to achieve the desired rotation efficiently.
      """
      n = len(nums)
      k %= n # k = k % n -> in case if k >= n
    
      def reverse(start: int, end: int) -> None:
          while start < end:
              nums[start], nums[end] = nums[end], nums[start]
              start += 1
              end -= 1

      reverse(0, n-1)
      reverse(0, k-1)
      reverse(k, n-1)
