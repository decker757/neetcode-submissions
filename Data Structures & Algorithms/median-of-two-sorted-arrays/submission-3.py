class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)

        merged = nums1 + nums2
        merged.sort()

        if (n + m) % 2 != 0:
            return merged[len(merged) // 2]
        else:
            return (merged[len(merged) // 2 - 1] + merged[len(merged) // 2]) / 2.0
