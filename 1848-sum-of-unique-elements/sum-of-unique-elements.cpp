class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        unordered_map<int, int> mp;
        int res = 0;
        for (int n : nums) {
            mp[n]++;
        }
        
        for (const auto& [k, v] : mp) {
            if (v == 1) {
                res += k;
            }
        }

        return res;
    }
};