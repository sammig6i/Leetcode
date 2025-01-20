class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        vector<vector<int>> freq(arr.size() + 1);
        unordered_map<int, int> mp;

        for (int num : arr) {
            mp[num]++;
        }

        for (const auto& [k, v] : mp) {
            freq[v].push_back(k);
        }

        for (auto arr : freq) {
            if (arr.size() > 1) {
                return false;
            }
        }

        return true;
    }
};