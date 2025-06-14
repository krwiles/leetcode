class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_n = num
        min_n = num

        # max calculation
        # make the first non 9 digit 9
        n_str = str(num)
        for i in range(len(n_str)):
            if n_str[i] != '9':
                digit = n_str[i]
                n_str = n_str.replace(digit, '9')
                max_n = int(n_str)
                break

        # min calculation
        # because no leading zeros, always make the first digit 0
        n_str = str(num)
        digit = n_str[0]
        n_str = n_str.replace(digit, '0')
        min_n = int(n_str)

        return max_n - min_n
