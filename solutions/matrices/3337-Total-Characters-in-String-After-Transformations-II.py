import numpy as np


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 1_000_000_007

        # initialize transformation matrix and frequency vector
        # datatype object prevents integer overflow in numpy calculations
        T = np.zeros((26, 26), dtype=object)
        freq = np.zeros(26, dtype=object)

        # fill frequencies
        for char in s:
            freq[ord(char) - ord('a')] += 1

        # fill transformation matrix according to the problem
        for m in range(26):
            for n in range(nums[m]):
                T[(m + 1 + n) % 26][m] += 1

        # matrix multiplication with modulus
        def mat_mult_mod(A, B):
            return np.mod(np.matmul(A, B), MOD)

        # matrix binary exponentiation with modulus
        def mat_pow_mod(matrix, power):
            result = np.identity(matrix.shape[0], dtype=object)
            base = matrix % MOD

            while power > 0:
                if power % 2 == 1:
                    result = mat_mult_mod(result, base)
                base = mat_mult_mod(base, base)
                power //= 2

            return result % MOD

        T = mat_pow_mod(T, t)  # raise T to the t power to perform t operations
        freq = mat_mult_mod(T, freq)  # multiply the operations to the frequencies

        return int(sum(freq)) % MOD  # return the mod of the sum of frequencies
