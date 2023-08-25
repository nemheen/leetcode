class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        vector<vector<int>> res;

        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }

            int t = -nums[i];
            int l = i + 1;
            int r = nums.size() - 1;

            while (l < r) {
                int curr = nums[l] + nums[r];

                if (curr == t) {
                    res.push_back({nums[i], nums[l], nums[r]});

                    // Skip duplicates
                    while (l < r && nums[l] == nums[l + 1]) l++;
                    while (l < r && nums[r] == nums[r - 1]) r--;

                    l++;
                    r--;
                }  else if (curr < t) {
                    l++;
                } else {
                    r--;
                }
            }
        }
        return res;
    }
};

