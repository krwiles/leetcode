from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        diff = [0] * N  # difference array to record query operations

        # populate difference array
        for query in queries:
            l = query[0]
            r = query[1] + 1

            diff[l] += 1
            if r < N:
                diff[r] -= 1

        # prefix sum accumulation
        prefix = 0
        for i in range(N):
            prefix += diff[i]
            if nums[i] > prefix:  # if a number exceeds the sum of operations, it is not possible
                return False

        return True
