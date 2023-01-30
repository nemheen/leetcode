class Solution {
    public:
     int mySqrt(int x) {
        if(x==0) return 0;
        int start=1, end=x, ret=0;
        while(start<=end){
            int mid=start+(end-start)/2;
            if(x/mid==mid) return mid;
            else if(x/mid<mid){
                end=mid-1;
            }
            else{
                start=mid+1;
                ret=mid;
            }
           
        
    }
     return ret;

     }
     
};

