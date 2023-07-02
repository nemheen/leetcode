class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int zeros = 0;
        int n = nums.size();
        vector<int> res(n, 0);

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                zeros += 1;
            }
        }

        if (zeros > 1 || n <= 1) {
            return res;
        }

        if (zeros == 0) {
            int mul = 1;
            for (int j = 0; j < n; j++) {
                mul *= nums[j];
            }
            for (int k = 0; k < n; k++) {
                res[k] = mul / nums[k];
            }
        }

        if (zeros == 1) {
            int mul = 1;
            int i = 0;
            for(int i=0; i<n; i++) {
                if(nums[i] != 0) mul *= nums[i];
            }
            for (int j = 0; j < n; j++) {
                if (nums[j] == 0) {
                    res[j] = mul;
                } else {
                    res[j] = 0;
                }
            }
        }

        return res;
    }
};

