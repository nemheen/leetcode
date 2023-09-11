class Solution {
public:
    int maxProduct(vector<int>& nums) {
        priority_queue<int> pq(nums.begin(), nums.end());

        int p1 = pq.top()-1;
        pq.pop();
        int p2 = pq.top()-1;
        
        return p1*p2;
    }
};
