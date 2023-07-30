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
    vector<int>ret;
    void post(TreeNode* root) {
        
        if(root->left)  post(root->left);
        if(root->right)  post(root->right);
        ret.push_back(root->val);
    }
    vector<int> postorderTraversal(TreeNode* root) {
        
        if(root == NULL) return ret;
        post(root);
        return ret;
    }
};