class Solution {
public:
    bool isPalindrome(int x) {
        stack<int> stack; 
        
        if(x<0) return false;
        if(x==0) return true;
        int y = x;
        while(x){
            stack.push(x%10);
            x/=10;
        }
        while(y){
            if(stack.top() != y%10) return false;
            stack.pop();
            y/=10;
        }
        return true;
    }
};
