class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        int res = 0, curr = 0, cost = 0;
        int n = s.size();

        for (int i = 0, j = 0; j < n; ++j) {
            cost = abs(s[j] - t[j]);
            curr += cost;

            while (curr > maxCost) {
                curr -= abs(s[i] - t[i]);
                ++i;
            }

            res = max(res, j - i + 1);
        }
        return res;
    }
};