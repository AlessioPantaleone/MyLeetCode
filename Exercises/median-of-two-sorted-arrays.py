"""
Trting for less than O(n) time
i wanna kill myself
NOT WORKING AT THIS TIME
"""

class Solution:
    def findMedianSortedArrays(self, nums1:[int], nums2:[int]) -> float:
        """
        :type nums1: list[int]
        :type nums2: list[int]
        """
        numcount = (len(nums1) + len(nums2))
        if numcount%2 == 0:
            toremove = numcount//2 - 1
        else:
            toremove = numcount//2

        for i in range(toremove):
            if nums1[0] < nums2[0]:
                median = nums1.pop(0)
            else:
                median = nums2.pop(0)

        if numcount%2 == 0:
            if nums1[0] < nums2[0]:
                median1 = nums1.pop(0)
            else:
                median1 = nums2.pop(0)
            if nums1[0] < nums2[0]:
                median2 = nums1.pop(0)
            else:
                median2 = nums2.pop(0)
            return median1+median2/2
        else:
            if nums1 and nums1[0] < nums2[0]:
                median = nums1.pop(0)
            else:
                median = nums2.pop(0)
            return median





    def findMedianSortedArraysHard(self, nums1: [int], nums2: [int]) -> float:
        for number in nums2:
            nums1.append(number)
        nums1.sort()

        if len(nums1) %2 == 0:
            return (nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2
        else:
            return nums1[len(nums1)//2]

if __name__ == "__main__":
    S = Solution()
    print(S.findMedianSortedArrays([1,2,3,3],[4,6,7,8]))

