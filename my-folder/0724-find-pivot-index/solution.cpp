class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sum = 0;
        for(int i=0; i< nums.size(); i++)
        {
            sum+= nums[i];
        }
        int temp = 0;
        int j=0;
        for(j=0; j< nums.size(); j++)
            if (temp* 2 == sum - nums[j])
                return j;
            else 
                temp += nums[j] ;  
        return -1;
    }
};
