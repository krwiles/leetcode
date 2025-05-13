class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 1_000_000_007
        freq = [0] * 27  # array to hold frequencies, where [26] is always 0

        # count frequencies of characters in s
        for char in s:
            freq[ord(char) - ord('a')] += 1

        # perform t operations
        for _ in range(t):
            z = freq[25]  # hold number of z's

            # iterate backwards and move characters up to the next letter
            # 'a' becomes freq[-1] which is always 0
            for i in range(25, -1, -1):
                freq[i] = freq[i - 1]

            if z:  # turn any z's into a's and b's
                freq[0] = z  # remember a is currently 0
                freq[1] = (freq[1] + z) % MOD

        return sum(freq) % MOD

