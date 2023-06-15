class Solution {
public:
    string mergeAlternately(string a, string b) {
        string ans = "";
        int n = max(a.length(), b.length());
        for(int i=0; i<n; i++) {
            if(i<a.length()) ans += a[i];
            if(i<b.length()) ans += b[i];

        }

        return ans;
        
    }
};


