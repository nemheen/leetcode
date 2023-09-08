class Solution {
public:
    int findJudge(int n, vector<vector<int>>& t) {
       vector<int>res(n+1, 0);
       if(n==1) return 1;

       for(int i=0; i<t.size(); i++) {
           res[t[i][0]]--;
           res[t[i][1]]++;
       }
       for(int i=0; i<=n; i++) {
           if (res[i] == n-1) return i;
       }

       return -1;
    }

};
