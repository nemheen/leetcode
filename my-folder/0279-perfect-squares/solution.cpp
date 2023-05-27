class Solution {
public:
    int numSquares(int n) {
        unordered_map<int, int> dp; // dp map to store already calculated values
        return getMinSquares(n, dp);
    }

    int getMinSquares(int n, unordered_map<int, int>& dp) {
        if (n <= 0) return 0;

        if (dp.find(n) != dp.end()) return dp[n]; // Check if value already exists in dp map

        int minSquares = INT_MAX;
        for (int i = 1; i * i <= n; i++) {
            int currSquares = getMinSquares(n - i * i, dp) + 1;
            minSquares = min(minSquares, currSquares);
        }

        dp[n] = minSquares; // Store the calculated value in dp map

        return minSquares;
    }
};

