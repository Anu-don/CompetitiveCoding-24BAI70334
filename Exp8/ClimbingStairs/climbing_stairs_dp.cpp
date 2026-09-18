// Experiment 8.1 - Climbing Stairs
// Approach: Bottom-up DP with two rolling variables
// LeetCode #70 | CC-II (24CSP-339)

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        int prev1 = 1, prev2 = 2;
        for (int i = 3; i <= n; i++) {
            int current = prev1 + prev2;
            prev1 = prev2;
            prev2 = current;
        }
        return prev2;
    }
};

int main() {
    cout << "================================================================\n";
    cout << "  CLIMBING STAIRS  |  Bottom-Up DP (O(n) / O(1))\n";
    cout << "  LeetCode #70  |  Experiment 8.1  |  C++\n";
    cout << "================================================================\n\n";

    Solution sol;
    vector<int> tests = {1, 2, 3, 4, 5, 6, 8, 10, 20, 45};
    for (int n : tests) {
        cout << "n = " << n << "\n";
        cout << "  Ways : " << sol.climbStairs(n) << "\n\n";
    }

    cout << "================================================================\n";
    cout << "  All test cases executed successfully.\n";
    cout << "================================================================\n";
    return 0;
}
