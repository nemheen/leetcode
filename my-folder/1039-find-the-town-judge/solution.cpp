class Solution {
public:
    int findJudge(int n, vector<vector<int>>& t) {
       vector<int>tcount(n+1, 0);

       if(t.empty() && n==1) return 1;
       for(int i=0; i<t.size(); i++) {
           tcount[t[i][0]]--;
           tcount[t[i][1]]++;

       }
       for(int i=0; i<n+1; i++) {
           if(tcount[i]==n-1) return i;
       }

       return -1;
    }

};
