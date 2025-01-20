class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        unordered_map<int, int> mp;
        int res = 0;
        for (int n : nums) {
            mp[n]++;
        }

        for (auto [n, freq] : mp) {
            res += freq * (freq-1) / 2;
        }
        return res;
    }
};