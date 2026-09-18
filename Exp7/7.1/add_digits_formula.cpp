// Experiment 7.1 - Add Digits
// Approach: Digital-root formula O(1)
// LeetCode #258 | CC-II (24CSP-339)

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int addDigits(int num) {
        if (num == 0) return 0;
        return 1 + (num - 1) % 9;
    }
};

int main() {
    cout << "================================================================\n";
    cout << "  ADD DIGITS  |  Digital Root Formula O(1)\n";
    cout << "  LeetCode #258  |  Experiment 7.1  |  C++\n";
    cout << "================================================================\n\n";

    Solution sol;
    vector<int> tests = {38, 0, 5, 99, 12345, 10, 100, 9, 18, 2147483647};
    for (int num : tests) {
        cout << "num = " << num << "\n";
        cout << "  Digital root : " << sol.addDigits(num) << "\n\n";
    }

    cout << "================================================================\n";
    cout << "  All test cases executed successfully.\n";
    cout << "================================================================\n";
    return 0;
}
