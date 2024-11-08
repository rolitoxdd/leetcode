import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> positions = new HashMap<>();
        for (int i = 0; i< nums.length; i++) {
            int n = nums[i];
            positions.put(n, i);
        }
        int[] res = new int[2];

        for (int i = 0; i< nums.length; i++) {
            int complement = target - nums[i];
            if (positions.containsKey(complement) && i != positions.get(complement)) {
                res[0] = i;
                res[1] = positions.get(complement);
            }
        }

        return res;
    }
    

}