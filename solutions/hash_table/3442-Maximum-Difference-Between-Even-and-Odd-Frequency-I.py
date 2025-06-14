from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)  # Count frequencies
        max_odd = 0
        min_even = 101  # Max size of s is 100

        for freq in count.values():
            if freq & 1 == 0:  # if frequency is even
                min_even = min(min_even, freq)
            else:
                max_odd = max(max_odd, freq)

        return max_odd - min_even
