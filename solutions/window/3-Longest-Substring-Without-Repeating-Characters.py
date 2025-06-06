class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0  # store the maximum window size
        count = set()  # keep track of characters in window
        l = 0  # left pointer of window

        # increment right pointer through the string
        for r in range(len(s)):
            # if a duplicate character is found
            if s[r] in count:
                maximum = max(maximum, r - l)  # record maximum

                # increment left pointer and remove characters until the duplicate is removed
                while s[r] in count:
                    count.remove(s[l])
                    l += 1

            # add the character to the set
            count.add(s[r])

        # return max of the recorded maximum and the final window
        return max(maximum, len(s) - l)
