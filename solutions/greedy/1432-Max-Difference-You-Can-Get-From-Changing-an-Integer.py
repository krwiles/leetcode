class Solution:
    def maxDiff(self, num: int) -> int:
        # MAX: Replace the first non 9 digit with 9
        n_str = str(num)
        for i in range(len(n_str)):
            if n_str[i] != '9':
                d = n_str[i]
                n_str = n_str.replace(d, '9')
                break
        max_n = int(n_str)

        # MIN: Two cases:
        n_str = str(num)
        # Leading digit is already 1
        if n_str[0] == '1':
            # Replace first non 0, non 1 digit with 0
            for i in range(1, len(n_str)):
                if int(n_str[i]) > 1:
                    d = n_str[i]
                    n_str = n_str.replace(d, '0')
                    break
        # Leading digit is not 1
        else:
            d = n_str[0]
            n_str = n_str.replace(d, '1')  # Make leading digit 1
        min_n = int(n_str)

        return max_n - min_n
