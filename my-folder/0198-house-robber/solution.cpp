class Solution {
public:
    int rob(vector<int>& nums) {
       
        int n = nums.size();
        int a = 0, b = 0;
        for (int i = 0; i< n; i++)
        {
            int temp = a;
            a = max(a, b + nums[i]);
            b = temp;
        }
        return a;
    }
};
