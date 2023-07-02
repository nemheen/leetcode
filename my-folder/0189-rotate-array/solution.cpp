class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n;
        
        vector<int> nums1(nums.begin() + (n - k), nums.end());
        vector<int> nums2(nums.begin(), nums.begin() + (n - k));
        
        nums = nums1;
        nums.insert(nums.end(), nums2.begin(), nums2.end());
    }
};
