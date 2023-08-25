class Solution {
public:
    int maxArea(vector<int>& h) {
        if(h.size() < 2) return 0;
        int l=0;
        int r=h.size()-1;
        int res = -1;
        while(l<r) {
            int area = min(h[r], h[l])*(r-l);
            res = max(res, area);
            if(h[r] > h[l]) l++;
            else r--;
        }
        return res;
    }
};
