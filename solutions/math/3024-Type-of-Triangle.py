from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:

        equal = 0
        for i in range(3):
            if nums[i] == nums[i - 1]:  # count the number of equal sides
                equal += 1
            if nums[i] + nums[i - 1] <= nums[i - 2]:  # check if any one side is bigger than the other two
                return "none"

        # return the type of triangle based on the number of equal sides
        if equal == 0:
            return "scalene"
        if equal == 1:
            return "isosceles"
        if equal > 1:
            return "equilateral"
