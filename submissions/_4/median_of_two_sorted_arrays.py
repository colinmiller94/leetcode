class Solution:

    @staticmethod
    def _median(array):
        length = len(array)
        if length % 2 == 0:
            return (array[length // 2] + array[length // 2 - 1]) / 2.0
        return array[length // 2]

    def findMedianSortedArrays(self, nums1, nums2):


        results = []
        while nums1 or nums2:
            if not nums1:
                results.append(nums2[0])
                nums2 = nums2[1:]
                continue

            if not nums2:
                results.append(nums1[0])
                nums1 = nums1[1:]
                continue

            if nums1[0] < nums2[0]:
                results.append(nums1[0])
                nums1 = nums1[1:]
                continue
            results.append(nums2[0])
            nums2 = nums2[1:]

        return self._median(results)