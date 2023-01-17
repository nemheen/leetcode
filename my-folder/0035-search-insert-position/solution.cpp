class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n= nums.size();
        int i, res;
        if(nums[n-1]<target) return n;
        if(nums[0]>target) return 0;
        for (i=0; i< n-1; i++){
        
           if(target<nums[i] || target==nums[i]) {
                res=i;
                break;
            }
        }
        return res;
    
    }
};
