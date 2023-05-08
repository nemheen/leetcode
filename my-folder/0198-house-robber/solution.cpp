class Solution {
public:
    int rob(vector<int>& nums) {
       
        int n = nums.size();
        vector<int> rob(n, 0);
        if(n==1) {
          return nums[0];
        }
        rob[0] = nums[0];
        rob[1] = nums[1];
        for(int i=2; i<n; i++) {
          if(i>2) {
              rob[i] = nums[i]+max(rob[i-2], rob[i-3]);
          }
          else {
            rob[i] = nums[i]+rob[i-2];
          }
        }
        return max(rob[n-1], rob[n-2] );
         
    }
};
