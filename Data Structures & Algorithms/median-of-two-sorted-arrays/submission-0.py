class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        odd = (len(nums1) + len(nums2)) % 2 == 1
        l1, l2 = 0, 0
        r1, r2 = len(nums1) - 1, len(nums2) - 1

        while r1 - l1 >= 2 and r2 - l2 >= 2:
            mid1, mid2 = (l1 + r1) // 2, (l2 + r2) // 2
            if nums1[mid1] > nums2[mid2]:
                k = min(r1 - mid1, mid2 - l2)
                r1 -= k
                l2 += k
            else:
                k = min(mid1 - l1, r2 - mid2)
                l1 += k
                r2 -= k

        rest = sorted(nums1[l1:r1 + 1] + nums2[l2:r2 + 1])
        N = len(rest)
        if odd:
            return float(rest[N // 2])
        else:
            return (rest[N // 2 - 1] + rest[N // 2]) / 2