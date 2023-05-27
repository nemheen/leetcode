class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        unordered_map<int, int> dp; // DP map to store already calculated values
        return getMinCoins(amount, coins, dp);
    }

    int getMinCoins(int amount, vector<int>& coins, unordered_map<int, int>& dp) {
        if (amount == 0) return 0;
        if (dp.find(amount) != dp.end()) return dp[amount];

        int minCoins = INT_MAX;
        for (int coin : coins) {
            if (coin <= amount) {
                int remainingAmount = amount - coin;
                int currCoins = getMinCoins(remainingAmount, coins, dp);
                if (currCoins != -1) {
                    minCoins = min(minCoins, currCoins + 1);
                }
            }
        }

        dp[amount] = (minCoins == INT_MAX) ? -1 : minCoins;
        return dp[amount];
    }
};

