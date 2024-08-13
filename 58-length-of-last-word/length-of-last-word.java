class Solution {
    public int lengthOfLastWord(String s) {
        boolean foundWord = false;
        int counter = 0;
        for (int i = s.length()-1; i>=0 ;i--) {
            if (foundWord == true && s.charAt(i) == ' ') {
                break;
            } else if (s.charAt(i) != ' ') {
                foundWord = true;
                counter ++;
            }
        }
        return counter;
    }
}