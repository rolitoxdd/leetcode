class Solution {
    public int lengthOfLastWord(String s) {
        boolean wordFound = false;
        int counter = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) != ' ') {
                counter++;
                wordFound = true;
            } else if (wordFound == true) {
                break;
            }
        }
        return counter;
    }
}