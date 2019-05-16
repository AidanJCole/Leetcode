class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        cat = nums1+nums2
        cat.sort()
        l = len(cat)
        if l % 2 == 0:
             return (cat[int(l/2-1)] + cat[int(l/2)]) / 2
        else:
            return cat[int((l-1)/2)]