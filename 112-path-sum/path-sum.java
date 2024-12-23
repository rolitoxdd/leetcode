/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null ) {
            return false;
        }
        int newTarget = targetSum - root.val;
        if (newTarget == 0 && root.left == null && root.right == null ) {
            return true;
        } else {
            if (root.left != null && hasPathSum(root.left, newTarget)) {
                return true;
            }
            if (root.right != null && hasPathSum(root.right, newTarget)) {
                return true;
            }
            return false;
        } 
    }
}