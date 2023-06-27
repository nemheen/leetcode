class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int n = (int) candies.size();
        int mx = candies[0];
        for(int i=1;i<n;i++){
          if(mx<candies[i]){
               mx=candies[i];
          }
         }
        vector<bool> res(n, false);
        for (int i=0; i<n; i++)
        {
          if(candies[i] + extraCandies >= mx) 
          {
            res[i] = true;
          }
        }
        return res;
    }
};
