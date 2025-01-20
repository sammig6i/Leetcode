class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        unordered_map<int, int> mp;
        int res = 0;
        for (int n : nums) {
            mp[n]++;
        }
        
        for (const auto& pair : mp) {
            if (pair.second == 1) {
                res += pair.first;
            }
        }

        return res;
    }
};