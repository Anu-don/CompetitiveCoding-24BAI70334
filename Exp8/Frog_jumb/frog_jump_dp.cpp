// Experiment 8.2 - Frog Jump with K Distance
// Approach: Bottom-up 1-D DP
// CC-II (24CSP-339)

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCost(vector<int>& height, int k) {
        int n = (int)height.size();
        vector<int> dp(n, 0);
        for (int i = 1; i < n; i++) {
            int best = INT_MAX;
            for (int j = max(0, i - k); j < i; j++) {
                int cost = dp[j] + abs(height[i] - height[j]);
                best = min(best, cost);
            }
            dp[i] = best;
        }
        return dp[n - 1];
    }
};

int main() {
    cout << "================================================================\n";
    cout << "  FROG JUMP WITH K DISTANCE  |  Bottom-Up 1-D DP\n";
    cout << "  Experiment 8.2  |  C++\n";
    cout << "================================================================\n\n";

    Solution sol;
    vector<pair<vector<int>, int>> cases = {
        {{10, 30, 40, 50, 20}, 3},
        {{10, 20, 10}, 1},
        {{30, 10, 60, 10, 60, 50}, 2},
        {{40}, 1},
        {{10, 10, 10, 10}, 3},
    };
    for (auto& c : cases) {
        cout << "height = [";
        for (size_t i = 0; i < c.first.size(); i++) {
            if (i) cout << ", ";
            cout << c.first[i];
        }
        cout << "], k = " << c.second << "\n";
        cout << "  Min cost : " << sol.minCost(c.first, c.second) << "\n\n";
    }

    cout << "================================================================\n";
    cout << "  All test cases executed successfully.\n";
    cout << "================================================================\n";
    return 0;
}
