/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rob(TreeNode* root) {
        unordered_map<TreeNode*, int> dp; //dp={} in python
        return dfs(root, dp);
    }

    int dfs(TreeNode* root, unordered_map<TreeNode*, int>&dp) {
        if(!root) return 0;

        if(dp.find(root) != dp.end()) return dp[root]; //root is already in dp and found, no need to calcualte so just return dp[root]
        
        int current = root->val;
        int left = 0, right = 0;
       

        if (root->left) {
            left = dfs(root->left->left, dp) + dfs(root->left->right, dp);
        }

        if(root->right) {
            right = dfs(root->right->left, dp) + dfs(root->right->right, dp);
        }

        current += left + right;
        int skip = dfs(root->left, dp) + dfs(root->right, dp);

        dp[root] = max(current, skip);

        return dp[root];

    }
};
