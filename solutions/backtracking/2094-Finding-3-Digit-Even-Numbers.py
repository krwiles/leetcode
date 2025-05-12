from typing import List


class Solution:
    # initialize variables used in the recursion
    def __init__(self) -> None:
        self.dig = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.num = [-1, -1, -1]
        self.ans = []

    # recursive backtracking function to construct all possible even numbers
    # it constructs the numbers in ascending order as required by the problem
    def backtrack(self, i: int) -> None:

        # base case: a number has been constructed, add it to the answer array
        if i > 2:
            self.ans.append(int(''.join(map(str, self.num))))
            return

        # main loop through all digits
        start = 1 if i == 0 else 0  # no leading zeros
        step = 2 if i == 2 else 1  # only even numbers
        for n in range(start, 10, step):
            # skip if none of that digit are available
            if self.dig[n] == 0:
                continue

            self.dig[n] -= 1  # use digit
            self.num[i] = n
            self.backtrack(i + 1)  # recursive call
            self.dig[n] += 1  # replace digit

    # main function
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # fill dig array with counts of digits
        for digit in digits:
            self.dig[digit] += 1

        # call backtracking function
        self.backtrack(0)

        return self.ans
