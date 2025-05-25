package solutions.matrices;

class Solution {
    public int longestPalindrome(String[] words) {
        // initialize matrix to count pairs
        int[][] matrix = new int[26][26];
        int ans = 0;

        // fill matrix 
        for (String w: words) {
            int m = w.charAt(0) - 'a';
            int n = w.charAt(1) - 'a';
            matrix[m][n]++;
        }

        // count all pairs of palindromes and add them to the answer
        for (int i = 0; i < 25; i++) {
            for (int j = i + 1; j < 26; j++) {
                if (matrix[i][j] > 0 && matrix[j][i] > 0) {
                    ans += 4 * Math.min(matrix[i][j], matrix[j][i]);  // 4 characters for each match
                }
            }
        }

        // count all equal pairs
        boolean odd = false;
        for (int i = 0; i < 26; i++) {
            if (matrix[i][i] % 2 == 1) {
                odd = true;
            }
            ans += 4 * (matrix[i][i] / 2);  // 4 characters per pair
        }
        if (odd) {
            ans += 2; // add 2 characters in the middle if an odd set exsists
        }  

        return ans;
    }
}