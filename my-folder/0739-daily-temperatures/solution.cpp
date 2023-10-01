class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temp) {
        stack<int> st;  // Use stack instead of vector
        int n = temp.size();
        vector<int> out(n, 0);

        for (int i = 0; i < n; i++) {
            while (!st.empty() && temp[i] > temp[st.top()]) {
                int j = st.top();
                st.pop();
                out[j] = i - j;
            }
            st.push(i);
        }

        return out;
    }
};

