// Experiment 7.1 - Add Digits
// Approach: Brute Force simulation
// LeetCode #258 | CC-II (24CSP-339)

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int addDigits(int num) {
        while (num >= 10) {
            int total = 0;
            while (num > 0) {
                total += num % 10;
                num /= 10;
            }
            num = total;
        }
        return num;
    }
};

int main() {
    cout << "================================================================\n";
    cout << "  ADD DIGITS  |  Brute Force (simulate digit sums)\n";
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
