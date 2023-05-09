class Solution {
public:
    bool wordBreak(string s, vector<string>& dict) {
        unordered_set<string> bag(dict.begin(), dict.end());
        unordered_map<int, bool> cache;
		
        // Define a recursive function to solve the problem
        function<bool(int)> go = [&](auto start) {
            // Base case: if we have reached the end of the string, return true
            if (start == s.size()) return true;
            // Check if we have already solved this subproblem
            if (cache.count(start)) return cache[start];
            
            // Otherwise, try all possible ways to split the string from the current position
            bool is_possible = false;
            string builder = "";
            for (int i = start; i < s.size(); i++) {
                builder += s[i];
                if (bag.count(builder)) is_possible |= go(i + 1);
            }
            // Memoize the result of this subproblem and return it
            return cache[start] = is_possible;
        };
		
        // Solve the problem starting from the beginning of the string
        return go(0);
    }
};
