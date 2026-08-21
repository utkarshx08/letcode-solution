import random

class Solution:
    def findKthLargest(self, nums, k):
        # Convert kth largest to index of kth smallest
        target = len(nums) - k

        left = 0
        right = len(nums) - 1

        while left <= right:

            # Choose a random pivot
            pivot = nums[random.randint(left, right)]

            # 3-way partition:
            # [less than pivot] [equal to pivot] [greater than pivot]
            low = left
            mid = left
            high = right

            while mid <= high:

                if nums[mid] < pivot:
                    nums[low], nums[mid] = nums[mid], nums[low]
                    low += 1
                    mid += 1

                elif nums[mid] > pivot:
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high -= 1

                else:
                    mid += 1

            # Target is in the left part
            if target < low:
                right = low - 1

            # Target is in the right part
            elif target > high:
                left = high + 1


            else:
                return pivot