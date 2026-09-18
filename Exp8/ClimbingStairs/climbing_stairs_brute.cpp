// Experiment 8.1 - Climbing Stairs
// Approach: Brute Force recursion
// LeetCode #70 | CC-II (24CSP-339)

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        return climbStairs(n - 1) + climbStairs(n - 2);
    }
};

int main() {
    cout << "================================================================\n";
    cout << "  CLIMBING STAIRS  |  Brute Force Recursion\n";
    cout << "  LeetCode #70  |  Experiment 8.1  |  C++\n";
    cout << "================================================================\n\n";

    Solution sol;
    vector<int> tests = {1, 2, 3, 4, 5, 6, 8, 10};
    for (int n : tests) {
        cout << "n = " << n << "\n";
        cout << "  Ways : " << sol.climbStairs(n) << "\n\n";
    }

    cout << "================================================================\n";
    cout << "  All test cases executed successfully.\n";
    cout << "================================================================\n";
    return 0;
}
