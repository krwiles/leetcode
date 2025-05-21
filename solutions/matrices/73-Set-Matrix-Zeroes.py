from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # methodology: use the first row and col to store zero rows and cols
        # this will make space complexity O(1)

        M = len(matrix)
        N = len(matrix[0])

        m0, n0 = False, False  # variables record if the first row and col have any zeros initially

        # check first col
        for m in range(M):
            if matrix[m][0] == 0:
                n0 = True
                break

        # check first row
        for n in range(N):
            if matrix[0][n] == 0:
                m0 = True
                break

        # loop through all elements not in row/col 0
        for m in range(1, M):
            for n in range(1, N):
                if matrix[m][n] == 0:  # record row/col of zeros in the first row and col
                    matrix[0][n] = 0
                    matrix[m][0] = 0

        # check first col for zeros
        for m in range(1, M):
            if matrix[m][0] == 0:  # set entire row to zeros
                matrix[m] = [0] * N

        # check first row for zeros
        for n in range(1, N):
            if matrix[0][n] == 0:  # set entire col to zeros
                for m in range(M):
                    matrix[m][n] = 0

        if m0:  # set first row to zeros if it had zeros initially
            matrix[0] = [0] * N
            print(N)

        if n0:  # set first col to zeros if it had zeros initially
            for m in range(M):
                matrix[m][0] = 0
