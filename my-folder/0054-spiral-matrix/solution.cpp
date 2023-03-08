class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int top=0, bottom=matrix.size()-1;
        int left=0, right=matrix[0].size()-1;
        int dir=0;
        vector<int>res;

        while(top<=bottom and left<=right)
        {
            if(dir==0)
            {
                for(int i=left; i<=right; i++)
                res.push_back(matrix[top][i]);
                top++;
            }
            else if(dir==1)
            {
                for(int j=top; j<=bottom; j++)
                res.push_back(matrix[j][right]);
                right--;
            }
            else if(dir==2)
            {
                for(int k=right; k>=left; k--)
                res.push_back(matrix[bottom][k]);
                bottom--;
            }
            else if(dir==3)
            {
                for(int l=bottom; l>=top; l--)
                res.push_back(matrix[l][left]);
                left++;
            }
            dir=(dir+1)%4;
        }
        return res;

    }
};
