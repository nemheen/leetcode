class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> hash;
        unordered_set<int>s;
        for (int num: arr) {
            hash[num]++;
            
        }

        int n = hash.size();

        for (const auto& pair : hash) {
            if (s.find(pair.second) != s.end()) {
                return false;
            }
            s.insert(pair.second);
        }

        return true;
    }
};
