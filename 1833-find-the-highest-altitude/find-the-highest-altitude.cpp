class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int n = gain.size();
        int res = 0;
        vector<int> prefix(n + 1);
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + gain[i];
        }

        for (int val : prefix) {
            res = max(res, val);
        }

        return res;
    }
};