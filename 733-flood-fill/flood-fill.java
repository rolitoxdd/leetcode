class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        boolean[][] visited = new boolean[image.length][image[sc].length];
        return aux(image, sr, sc, color, visited);
    }

    public int[][] aux(int[][] image, int sr, int sc, int color, boolean[][] visited) {
        if (visited[sr][sc]) return image;
        int originalColor = image[sr][sc];
        image[sr][sc] = color;
        visited[sr][sc] = true;
        if (sr - 1 >= 0 && image[sr - 1][sc] == originalColor) {
            // dfs
            aux(image, sr - 1, sc, color, visited);
        }
        if (sr + 1 < image.length && image[sr + 1][sc] == originalColor) {
            //dfs
            aux(image, sr + 1, sc, color, visited);

        }
        if (sc - 1 >= 0 && image[sr][sc-1] == originalColor) {
            aux(image, sr , sc - 1 , color, visited);

        }
        if (sc + 1 < image[sr].length && image[sr][sc+1] == originalColor) {
            //dfs
            aux(image, sr , sc + 1, color, visited);
        }
        return image;
    }
}