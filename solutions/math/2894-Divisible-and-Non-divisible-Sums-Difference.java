package solutions.math;

class Solution {
    // outputs sum of all integers up to n
    public int sumOfInts(int n) {
        return (n * n + n) / 2;
    }
    
    public int differenceOfSums(int n, int m) {
        // if m is 1 simply return negative sum of n
        if (m == 1) {
            return -sumOfInts(n);
        }
        
        // manually sum integers with setp m up to n
        int mSum = 0;
        for (int i = m; i <= n; i += m) {
            mSum += i;
        }

        // return sum of ints not divisible by m minus the sum of ints divisible by m
        // the same as the sum of ints up to n minus 2x the sum of ints divisible by m
        return sumOfInts(n) - 2*mSum;
    }
}