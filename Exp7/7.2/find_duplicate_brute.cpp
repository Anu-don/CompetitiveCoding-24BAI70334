// Experiment 7.2 - Find the Duplicate Number
// Approach: Brute Force hash set
// LeetCode #287 | CC-II (24CSP-339)

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int x : nums) {
            if (seen.count(x)) return x;
            seen.insert(x);
        }
        return -1;
    }
};

int main() {
    cout << "================================================================\n";
    cout << "  FIND THE DUPLICATE NUMBER  |  Brute Force (hash set)\n";
    cout << "  LeetCode #287  |  Experiment 7.2  |  C++\n";
    cout << "================================================================\n\n";

    Solution sol;
    vector<vector<int>> tests = {
        {1, 3, 4, 2, 2},
        {3, 1, 3, 4, 2},
        {3, 3, 3, 3, 3},
        {1, 1},
        {2, 5, 9, 6, 9, 3, 8, 9, 7, 1},
    };
    for (auto nums : tests) {
        cout << "nums = [";
        for (size_t i = 0; i < nums.size(); i++) {
            if (i) cout << ", ";
            cout << nums[i];
        }
        cout << "]\n";
        cout << "  Duplicate : " << sol.findDuplicate(nums) << "\n\n";
    }

    cout << "================================================================\n";
    cout << "  All test cases executed successfully.\n";
    cout << "================================================================\n";
    return 0;
}
