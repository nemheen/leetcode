class Solution {
public:
    bool isSubsequence(string s, string t) {
            int j=0, i=0;
            while(t[i]){
                if(s[j]!= t[i])
                i++;
                else {
                    i++;
                    j++;
                }
        }
         if(j==s.size() && i==t.size()) return true;
         else return false;

        
    }
};
