from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        for i in range(0, len(s), k):  # Append segments of size k
            end = min(i + k, len(s))  # Adjust segment for the end of the string
            ans.append(s[i:end])

        ans[-1] += fill * (k - len(ans[-1]))  # Fill the final segment to reach size k

        return ans
