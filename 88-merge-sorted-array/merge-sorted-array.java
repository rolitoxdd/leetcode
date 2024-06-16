class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] res = new int[n+m];
        int c1 = 0, c2 = 0;
        for (int i = 0; i < n+m; i++){
            if ((nums2.length == 0  || c2 >= n)|| (c1 < m && nums1[c1] < nums2[c2]
            )) {
                res[i] = nums1[c1];
                c1++;
            } else {
                res[i] = nums2[c2];
                c2++;
            }
        }
        
        for (int i = 0; i< n+m; i++) {
            nums1[i] = res[i];
        }
    }
}