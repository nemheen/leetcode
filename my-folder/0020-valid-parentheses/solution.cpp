class Solution {
public:
    bool isValid(string s) {
        int i, n, j=0;
        stack<char> stack;
        n = s.size();
        if(n == 0) return true;
        if(n%2 != 0) return false;
        for(i=0; i<n; i++) {
            if(s[i] == '(' || s[i] == '{' || s[i] == '[') {
                stack.push(s[i]);
            }
            else if ( (s[i] == ')' && !stack.empty() && stack.top() == '(') ||
                        (s[i] == '}' && !stack.empty() && stack.top() == '{') ||
                        (s[i] == ']' && !stack.empty() && stack.top() == '[')
                      ){ stack.pop(); }
            else return false;
            }
        if(stack.empty()) return true;
        return false;  
    }
};
