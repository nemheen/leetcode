class Solution {
public:
    double myPow(double x, long n) {
        double res = 1.0;
        char neg = false;

        if (n==0) return 1;
        if (n < 1) { 
            neg = true;
            n = -n;   
        }
        
        while(n > 0)
        {
            if(n%2 == 1) {
                res *= x;
            }
            x *= x;
            n /= 2;
        }
        if(neg){
            return 1/res;
        }
        else {
            return res;
        }
    }
};
