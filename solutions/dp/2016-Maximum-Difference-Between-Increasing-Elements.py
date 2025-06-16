from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minimum = nums[0]
        max_diff = -1

        # Compare each number to the current minimum
        for num in nums:
            if num > minimum:
                max_diff = max(max_diff, num - minimum)
            else:
                minimum = num

        return max_diff
