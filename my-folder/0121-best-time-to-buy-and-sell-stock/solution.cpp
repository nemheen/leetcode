class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ret=0;
        int minimum = prices[0];

        for(int i=0; i<prices.size()-1; i++){
            if(prices[i+1]>prices[i]) ret = max(ret, prices[i+1]-minimum);
            else minimum=min(minimum, prices[i+1]);
        }
        return ret;
    }
};
