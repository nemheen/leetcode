class Solution {
public:
    bool wordBreak(string s, vector<string>& dict) {
       int n = s.length();
       unordered_set<string> word(dict.begin(), dict.end());

       vector<bool> dp(n+1, false);
       dp[0] = true;

       for(int i=0; i<=n; i++) {
           for(int j=0; j<i; j++) {
               if(dp[j] && word.count(s.substr(j, i-j))) {
                   dp[i] = true;
                 
               }
           }
       }
        return dp[n];


    }
};
