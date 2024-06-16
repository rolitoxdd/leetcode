class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                res[k] = nums[i];
                k++;
            } 
        }
        for (int i = 0; i< res.length; i++) {
            nums[i] =res[i];
        }
        return k;
        
    }
}