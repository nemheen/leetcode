class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int , int>> pairs;
        for(int i=0; i<speed.size(); i++)  {
            pairs.push_back({position[i], speed[i]});
        }
        sort(pairs.begin(), pairs.end());

        int fleet=0;
        vector<float>times;
        for(int i=0; i<pairs.size(); i++){
            times.push_back((target*1.0 - pairs[i].first*1.0)/(pairs[i].second*1.0));
        }
        float curr = INT_MIN;
        for(int i=times.size()-1; i>=0; i--) {
            if(times[i] > curr) {
                curr = times[i];
                fleet += 1;

            }
        }
        return fleet;
    }
};
