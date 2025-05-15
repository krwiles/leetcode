from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # the greedy solution works for this problem

        ans = [words[0]]  # initialize array of answers with the first value
        prev = groups[0]  # initialize previous value from groups

        # loop through remaining values, and greedily take each differing value
        for i in range(1, len(words)):
            if groups[i] != prev:
                ans.append(words[i])
                prev = groups[i]  # set new previous value

        return ans
