// Experiment 6.1 - LCA of a Binary Tree
// Approach: Brute Force (two root-to-node paths)
// LeetCode #236 | CC-II (24CSP-339)

#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

TreeNode* buildTree(const vector<string>& vals) {
    if (vals.empty() || vals[0] == "#" || vals[0] == "null") return nullptr;
    vector<TreeNode*> nodes;
    for (auto& v : vals) {
        if (v == "#" || v == "null") nodes.push_back(nullptr);
        else nodes.push_back(new TreeNode(stoi(v)));
    }
    size_t i = 0, child = 1;
    while (child < nodes.size()) {
        if (nodes[i]) {
            if (child < nodes.size()) nodes[i]->left = nodes[child++];
            if (child < nodes.size()) nodes[i]->right = nodes[child++];
        }
        i++;
    }
    return nodes[0];
}

TreeNode* findNode(TreeNode* root, int val) {
    if (!root) return nullptr;
    if (root->val == val) return root;
    TreeNode* L = findNode(root->left, val);
    return L ? L : findNode(root->right, val);
}

bool pathTo(TreeNode* node, TreeNode* target, vector<TreeNode*>& trail) {
    if (!node) return false;
    trail.push_back(node);
    if (node == target) return true;
    if (pathTo(node->left, target, trail) || pathTo(node->right, target, trail))
        return true;
    trail.pop_back();
    return false;
}

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        vector<TreeNode*> path1, path2;
        pathTo(root, p, path1);
        pathTo(root, q, path2);
        int i = 0;
        while (i < (int)path1.size() && i < (int)path2.size() && path1[i] == path2[i])
            i++;
        return path1[i - 1];
    }
};

int main() {
    cout << "================================================================\n";
    cout << "  LCA OF BINARY TREE  |  Brute Force (two paths)\n";
    cout << "  LeetCode #236  |  Experiment 6.1  |  C++\n";
    cout << "================================================================\n\n";

    Solution sol;
    vector<pair<vector<string>, pair<int,int>>> cases = {
        {{"3","5","1","6","2","0","8","#","#","7","4"}, {5,1}},
        {{"3","5","1","6","2","0","8","#","#","7","4"}, {5,4}},
        {{"1","2"}, {1,2}},
        {{"3","5","1","6","2","0","8"}, {6,8}},
        {{"3","5","1","6","2","0","8","#","#","7","4"}, {7,4}},
    };

    for (auto& c : cases) {
        TreeNode* root = buildTree(c.first);
        TreeNode* p = findNode(root, c.second.first);
        TreeNode* q = findNode(root, c.second.second);
        TreeNode* ans = sol.lowestCommonAncestor(root, p, q);
        cout << "Tree (level-order): [";
        for (size_t i = 0; i < c.first.size(); i++) {
            if (i) cout << ", ";
            cout << c.first[i];
        }
        cout << "]\n";
        cout << "  p = " << c.second.first << ", q = " << c.second.second << "\n";
        cout << "  LCA  : " << (ans ? to_string(ans->val) : "null") << "\n\n";
    }

    cout << "================================================================\n";
    cout << "  All test cases executed successfully.\n";
    cout << "================================================================\n";
    return 0;
}
