class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                char cell = grid[i][j];
                if (cell == '1') {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }

    public void dfs(char[][] grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length) return;
        char cell = grid[i][j];
        if (cell == '0' || cell == 'x') return;
        grid[i][j] = 'x';
        dfs(grid, i - 1, j);
        dfs(grid, i + 1 ,j);
        dfs(grid, i, j - 1);
        dfs(grid, i, j + 1);
    }
}