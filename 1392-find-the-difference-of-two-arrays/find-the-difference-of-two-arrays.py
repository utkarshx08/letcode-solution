class Solution:
    def findDifference(self, nums1, nums2):

        set1 = set(nums1)
        set2 = set(nums2)

        ans1 = list(set1 - set2)
        ans2 = list(set2 - set1)

        return [ans1, ans2]