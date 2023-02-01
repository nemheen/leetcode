class Solution {
public:
    int fib(int n) {
        int n_2 = 0;
        int n_1 = 1;
        int fib = 0;
        if(n<2) return n;
        
       else{
            for(int i = 1; i < n; i++){
            fib = n_2 + n_1;
           n_2 = n_1;
           n_1 = fib;
           }
       }
        return fib;

    }
};
