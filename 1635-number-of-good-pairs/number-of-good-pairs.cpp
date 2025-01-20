class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        unordered_map<int, int> mp;
        int res = 0;
        for (int n : nums) {
            mp[n]++;
        }

        for (auto [n, count] : mp) {
            res += (count * (count - 1)) / 2;
        }

        return res;
    }
};