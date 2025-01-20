class Solution {
public:
    int findLucky(vector<int>& arr) {
        int res = -1;
        unordered_map<int, int> mp;
        for (int n : arr) {
            mp[n]++;
        }

        for (const auto& [k, v] : mp) {
            if (k == v) {
                res = max(res, k);
            }
        }

        return res;
    }
};