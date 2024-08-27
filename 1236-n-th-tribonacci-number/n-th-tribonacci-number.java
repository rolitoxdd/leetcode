class Solution {
    public int[] memo;
    public int tribonacci(int n) {
        if (memo == null) {
            memo = new int[n+1];
        }
        if (n <=1) {
            return n;
        }  else if (n==2) {return 1;}else if (memo[n] != 0) {
            return memo[n];
        } else {
            memo[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3);
            return memo[n];
        }
        
    }
}