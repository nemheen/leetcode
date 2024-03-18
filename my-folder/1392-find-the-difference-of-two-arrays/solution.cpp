class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>>res;

        unordered_set<int>s1(nums1.begin(), nums1.end());
        unordered_set<int>s2(nums2.begin(), nums2.end());

        vector<int>d1;
        vector<int>d2;

        for (int num: s2) {
            if (s1.find(num) == s1.end()) {
                d1.push_back(num);
            }
        }

        for (int num: s1) {
            if (s2.find(num) == s2.end()) {
                d2.push_back(num);
            }
        }

        res = {d2, d1};

        return res;
    }
};
