class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        stack<int>st;

        if( nums.size() == 0) 
          return 0;
        int curr = 0, maxx = 0;

        sort(nums.begin(), nums.end());
        

        for(auto n: nums){
          if(!st.empty() && n-1 == st.top()){
            curr += 1;
            st.pop();
            st.push(n);
            maxx = max(maxx, curr);
          }
          else if(!st.empty() && st.top() == n) 
            continue;
          else {
            curr = 0;
            st.push(n);
          }
        }
        return maxx+1;
    }
};
