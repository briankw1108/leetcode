class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead. My version!
        """
        c = m+n-1
        m -= 1
        n -= 1
        while (m > -1) & (n > -1):
            if nums1[m] >= nums2[n]:
                nums1[c] = nums1[m]
                m -= 1
                c -= 1
            else:
                nums1[c] = nums2[n]
                n -= 1
                c-= 1
        if n > -1:
            for i in range(c+1):
                nums1[i] = nums2[i]

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead. Shorter solution from others.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
