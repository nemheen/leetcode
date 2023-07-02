class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();

        if(nums.empty()) return 0;

        sort(nums.begin(), nums.end());

        int most = 1, curr = 1;

        for (int i=1; i<n; i++)
        {
            if(nums[i] == nums[i-1] + 1) {
                curr += 1;
            } else if (nums[i] != nums[i-1])
            {
                most = max(curr, most);
                curr = 1;
            }
        }

        return max(most, curr);



    }


};

