class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {

        int n = score.size();
        vector<string>ans(n);

        map<int, int>m;


        for(int i=0; i<score.size(); i++){
            m[score[i]] = i;
        }
        
        priority_queue<int>pq(score.begin(), score.end());

        int x = 1;

        while(!pq.empty()) {
            int mx = pq.top(); pq.pop();
            if(x == 1) ans[m[mx]] = "Gold Medal";
            else if(x == 2) ans[m[mx]] = "Silver Medal";
            else if(x == 3) ans[m[mx]] = "Bronze Medal";

            else {
                ans[m[mx]] = to_string(x);
            }

            x++;
        }
        return ans;
    }
};
