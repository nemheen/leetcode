class Solution {
public:
    int trap(vector<int>& h) {
       
        int l=0, r = h.size()-1;
        int left = h[l], right = h[r];
        int res = 0;
        while(l<r) {
            if(left < right) {
                l++;
                left = max(left, h[l]);
                res += left - h[l];
            }
            else {
                r--;
                right = max(right, h[r]);
                res += right - h[r];
            }
        }
        return res;
    }
};
