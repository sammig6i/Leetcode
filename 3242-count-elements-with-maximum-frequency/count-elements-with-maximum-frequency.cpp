class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int, int> mp;
        int max_freq = 0, res = 0;
        for (int n : nums) {
            mp[n]++;
            max_freq = max(max_freq, mp[n]);
        }

        for (const auto& [k, v] : mp) {
            if (v == max_freq) {
                res += v;
            }
        }

        return res;
    }
};