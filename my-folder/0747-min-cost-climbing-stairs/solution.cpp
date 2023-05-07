class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        int size = n+2;
        int dp[size];
        memset(dp, 0, sizeof(dp));

        for(int i = n-1; i >=0; i--){
            dp[i] = cost[i] + min(dp[i+1], dp[i+2]);
        }
        return min(dp[0], dp[1]);
    }
};
