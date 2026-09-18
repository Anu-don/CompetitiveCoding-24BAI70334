// Experiment 6.2 - Inorder Successor in BST
// Approach: Brute Force (full in-order list)
// LeetCode #285 | CC-II (24CSP-339)

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

class Solution {
public:
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        vector<TreeNode*> order;
        function<void(TreeNode*)> inorder = [&](TreeNode* node) {
            if (!node) return;
            inorder(node->left);
            order.push_back(node);
            inorder(node->right);
        };
        inorder(root);
        for (size_t i = 0; i < order.size(); i++) {
            if (order[i] == p) {
                if (i + 1 < order.size()) return order[i + 1];
                return nullptr;
            }
        }
        return nullptr;
    }
};

int main() {
    cout << "================================================================\n";
    cout << "  INORDER SUCCESSOR IN BST  |  Brute Force (full in-order)\n";
    cout << "  LeetCode #285  |  Experiment 6.2  |  C++\n";
    cout << "================================================================\n\n";

    Solution sol;
    vector<pair<vector<string>, int>> cases = {
        {{"2","1","3"}, 1},
        {{"5","3","6","2","4","#","#","1"}, 6},
        {{"5","3","6","2","4","#","#","1"}, 3},
        {{"2","1","3"}, 2},
        {{"5","3","6","2","4","#","#","1"}, 2},
    };

    for (auto& c : cases) {
        TreeNode* root = buildTree(c.first);
        TreeNode* p = findNode(root, c.second);
        TreeNode* ans = sol.inorderSuccessor(root, p);
        cout << "BST (level-order): [";
        for (size_t i = 0; i < c.first.size(); i++) {
            if (i) cout << ", ";
            cout << c.first[i];
        }
        cout << "]\n";
        cout << "  p = " << c.second << "\n";
        cout << "  Successor : " << (ans ? to_string(ans->val) : "null") << "\n\n";
    }

    cout << "================================================================\n";
    cout << "  All test cases executed successfully.\n";
    cout << "================================================================\n";
    return 0;
}
