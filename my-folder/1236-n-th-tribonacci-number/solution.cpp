class Solution {
public:
    int tribonacci(int n) {
        if(n==0) return 0;
        if(n==1 || n==2) return 1;

        int n_3 = 0;
        int n_2 = 1;
        int n_1 = 1;
        int ret = 0;
        for(int i = 2; i < n; i++){
            ret = n_3 + n_2 + n_1;
            n_3 = n_2;
            n_2 = n_1;
            n_1 = ret;
        }
   
        return ret;

    }
};
