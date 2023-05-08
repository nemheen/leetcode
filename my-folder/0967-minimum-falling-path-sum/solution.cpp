class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& m) {
        int n = m.size();
        int minpath = INT_MAX;
      
        for(int i=1; i<n; i++) {
          for(int j=0; j<n; j++) {
              if(j==0) {
                  m[i][j] += min(m[i-1][j], m[i-1][j+1]);
              }
              else if(j==n-1) {
                m[i][j] += min(m[i-1][j-1], m[i-1][j]);
              }
              else {
                m[i][j] += min(min(m[i-1][j-1], m[i-1][j]), min( m[i-1][j], m[i-1][j+1] )); 
              }
          }
        }
        
        for( int j=0 ; j<n ; j++ ){
            minpath = min( minpath, m[n-1][j] );
        }

        return minpath ;


    }
};

