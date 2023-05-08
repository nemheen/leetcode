class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();

        vector<int> row(n, 0);
        row[0] = 1 - obstacleGrid[0][0];
        
        for (int j = 1; j < n; j++) {
            row[j] = obstacleGrid[0][j] == 0 ? row[j - 1] : 0;
        }
        
        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j] == 1) {
                    row[j] = 0;
                }
                else if (j > 0) {
                    row[j] += row[j - 1];
                }
            }
        }
        
        return row[n - 1];
    }
};

